# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from .internal_server_error_response import InternalServerErrorResponse


class InternalServerError(ApiError):
    def __init__(self, body: InternalServerErrorResponse):
        super().__init__(status_code=500, body=body)
