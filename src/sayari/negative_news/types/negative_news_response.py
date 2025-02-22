# This file was auto-generated by Fern from our API Definition.

import typing
from .article import Article

"""
from sayari.negative_news import Article

[
    Article(
        published="2024-09-15",
        risk_flags=[
            "Sanctions",
            "Regulatory Action",
            "Geopolitical Instability",
        ],
        search_term=[
            "Gazprom",
            [
                "sanctioned entity",
                "trade embargo",
                "international sanction",
                "restricted measures",
                "sanction violation",
                "trade restriction",
                "blacklisted entity",
                "economic sanction",
                "export control",
            ],
        ],
        snippet="Prime Ministers of Ukraine and Estonia Denys Shmyhal and Kristen Michal signed a joint statement calling for increased sanctions pressure on Russia and a full trade embargo. — Ukrinform.",
        source="@ukrinform",
        title="Ukraine, Estonia prime ministers call for imposing sanctions against Rosatom, Gazprom",
        url="https://www.ukrinform.net/rubric-polytics/3935996-ukraine-estonia-prime-ministers-call-for-imposing-sanctions-against-rosatom-gazprom.html",
    )
]
"""
NegativeNewsResponse = typing.List[Article]
