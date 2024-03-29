# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...base_types.types.paginated_response import PaginatedResponse
from .source import Source


class ListSourcesResponse(PaginatedResponse):
    """
    OK
    ---
    from sayari-analytics import (CountQualifier, Country, ListSourcesResponse,
                                  QualifiedCount, Source)

    ListSourcesResponse(offset=0, limit=2, size=QualifiedCount(count=521, qualifier=CountQualifier.EQ, ), next=True, data=[Source(id="f4396e4b8a41d1fd9f09ea94d2ebedb9", label="Online Registry Record", description="Contains profiles of registered companies. Provides standard company information including name, tax ID, status, address, and business purpose as well as current and former shareholders and directors.", country=Country.ARE, region="middle_east_&_africa", date_added="2023-07-25", source_type="company_data", record_type="company_record", structure="structured", source_url="https://www.website.com", pep=False, watchlist=False, ), Source(id="e85d865943ee6d8369307569d2ad9de0", label="Adverse Media Data", description="Contains PDFs and URLs to adverse media reporting for PEPs, SOEs, sanctioned entities, and entities linked to financial regulatory and law enforcement actions. Available for millions of entities.", country=Country.XXX, region="international_(multi-region_coverage)", date_added="2023-04-11", source_type="adverse_media_/_negative_news_data", record_type="adverse_media_record", structure="unstructured", source_url="https://www.website.com/", pep=False, watchlist=False, )], )
    """

    offset: int
    next: bool
    data: typing.List[Source]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
