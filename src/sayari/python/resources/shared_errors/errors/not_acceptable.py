# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.not_acceptable_response import NotAcceptableResponse


class NotAcceptable(ApiError):
    def __init__(self, body: NotAcceptableResponse):
        super().__init__(status_code=406, body=body)
