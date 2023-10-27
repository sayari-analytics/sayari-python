# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TranslationContext(str, enum.Enum):
    SAYARI_MACHINE_TRANSLATION = "sayari_machine_translation"
    """
    A translation made using a Sayari machine learning model
    """

    PINYIN = "pinyin"
    """
    A Pinyin transliteration
    """

    GOOGLE_TRANSLATE = "google_translate"
    """
    A translation made using Google Translate API
    """

    def visit(
        self,
        sayari_machine_translation: typing.Callable[[], T_Result],
        pinyin: typing.Callable[[], T_Result],
        google_translate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TranslationContext.SAYARI_MACHINE_TRANSLATION:
            return sayari_machine_translation()
        if self is TranslationContext.PINYIN:
            return pinyin()
        if self is TranslationContext.GOOGLE_TRANSLATE:
            return google_translate()
