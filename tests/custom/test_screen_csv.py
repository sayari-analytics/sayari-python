import csv
import time
from types import SimpleNamespace

import pytest
from sayari.client import Sayari

# These tests use a fake client, so they need no credentials and make no API calls.
#
# Row names decide what the fake API returns:
#   "clean-*"    resolves to an entity with no risk
#   "risky-*"    resolves to an entity with a real risk factor
#   "country-*"  resolves to an entity whose only risks are country-level (cpi_score, basel_aml)
#   "nomatch-*"  resolves to nothing
#   "boom-*"     makes the entity summary call raise
# Every resolvable row also returns a lower-scoring decoy match FIRST, so picking data[0] screens
# the wrong entity.


class FakeResolution:
    def resolution(self, name=None, **kwargs):
        label = name[0]
        if label.startswith("nomatch"):
            return SimpleNamespace(data=[])
        decoy = SimpleNamespace(entity_id="decoy", score=10.0)
        best = SimpleNamespace(entity_id=label, score=99.0)
        return SimpleNamespace(data=[decoy, best])


class FakeEntity:
    def __init__(self, delay):
        self.delay = delay

    def entity_summary(self, entity_id):
        time.sleep(self.delay)
        if entity_id == "decoy" or entity_id.startswith("risky"):
            risk = {"sanctioned": {}}
        elif entity_id.startswith("country"):
            risk = {"cpi_score": {}, "basel_aml": {}}
        elif entity_id.startswith("boom"):
            raise RuntimeError("simulated API failure")
        else:
            risk = {}
        return SimpleNamespace(label=entity_id, risk=risk)


def make_client(delay=0.0):
    # Build a real Sayari object (so screen_csv is the real method) without calling its constructor.
    client = Sayari.__new__(Sayari)
    client.resolution = FakeResolution()
    client.entity = FakeEntity(delay)
    return client


def write_csv(tmp_path, names):
    path = tmp_path / "rows.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Country"])
        for name in names:
            writer.writerow([name, "USA"])
    return str(path)


def labels(entities):
    return sorted(e.label for e in entities)


def test_every_row_is_returned(tmp_path):
    # The reported bug: 5 rows in, 4 results out (the last result was lost).
    names = ["clean-1", "clean-2", "risky-1", "clean-3", "nomatch-1"]
    risky, non_risky, unresolved = make_client(delay=0.3).screen_csv(write_csv(tmp_path, names))
    assert labels(risky) == ["risky-1"]
    assert labels(non_risky) == ["clean-1", "clean-2", "clean-3"]
    assert unresolved == [["nomatch-1", "USA"]]


def test_many_rows_are_not_dropped(tmp_path):
    names = [f"clean-{i}" for i in range(300)]
    risky, non_risky, unresolved = make_client().screen_csv(write_csv(tmp_path, names))
    assert len(non_risky) == 300
    assert risky == [] and unresolved == []


def test_best_scoring_match_is_screened_not_first(tmp_path):
    # The decoy comes first with a low score; the real match has the higher score.
    risky, non_risky, _ = make_client().screen_csv(write_csv(tmp_path, ["clean-1"]))
    assert risky == []
    assert labels(non_risky) == ["clean-1"]


def test_can_be_called_more_than_once(tmp_path):
    client = make_client()
    path = write_csv(tmp_path, ["clean-1", "risky-1"])
    for _ in range(2):
        risky, non_risky, unresolved = client.screen_csv(path)
        assert labels(risky) == ["risky-1"]
        assert labels(non_risky) == ["clean-1"]
        assert unresolved == []


def test_country_level_risks_count_as_risky_by_default(tmp_path):
    # Existing behaviour is kept unless the caller opts out.
    risky, non_risky, _ = make_client().screen_csv(write_csv(tmp_path, ["country-1"]))
    assert labels(risky) == ["country-1"]
    assert non_risky == []


def test_ignore_risk_factors(tmp_path):
    risky, non_risky, _ = make_client().screen_csv(
        write_csv(tmp_path, ["country-1", "risky-1"]),
        ignore_risk_factors=["cpi_score", "basel_aml"],
    )
    assert labels(risky) == ["risky-1"]
    assert labels(non_risky) == ["country-1"]


def test_worker_failure_is_not_silent(tmp_path):
    # A worker that dies must not look like a complete, successful screening.
    with pytest.raises(RuntimeError):
        make_client().screen_csv(write_csv(tmp_path, ["clean-1", "boom-1", "clean-2"]))
