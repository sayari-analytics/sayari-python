# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.unauthorized_response import UnauthorizedResponse


class Unauthorized(ApiError):
    def __init__(self, body: UnauthorizedResponse):
        super().__init__(status_code=401, body=body)