# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TranslationContextEnum(str, enum.Enum):
    SAYARI_MACHINE_TRANSLATION = "sayari_machine_translation"
    PINYIN = "pinyin"
    GOOGLE_TRANSLATE = "google_translate"

    def visit(
        self,
        sayari_machine_translation: typing.Callable[[], T_Result],
        pinyin: typing.Callable[[], T_Result],
        google_translate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TranslationContextEnum.SAYARI_MACHINE_TRANSLATION:
            return sayari_machine_translation()
        if self is TranslationContextEnum.PINYIN:
            return pinyin()
        if self is TranslationContextEnum.GOOGLE_TRANSLATE:
            return google_translate()
