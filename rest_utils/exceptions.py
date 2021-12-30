from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    NotFound,
    ValidationError,
)


class BaseException(Exception):
    """
    Internal exception base class that can be handled by the exception handler.
    """
    code = None
    error_details = None
    message = None
    context = None
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message="", context=None, code=None, error_details=None, *args, **kwargs):
        self.code = code or self.code
        self.error_details = error_details or self.error_details
        self.message = message or self.message or ""
        self.context = context or {}

        if kwargs:
            self.context.update(kwargs)

        if self.context and self.message:
            self.message = self.message.format(**self.context)

    def __str__(self):
        return str(self.message)


class BadRequestException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    code = "BAD_REQUEST"


class NotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    code = "NOT_FOUND"


class InvalidInputException(BadRequestException):
    code = "INVALID_INPUT"


class MethodNotAllowedException(BadRequestException):
    code = "METHOD_NOT_ALLOWED"


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    message = _('You do not have permission to perform this action.')
    code = 'PERMISSION_DENIED'


class ProductNotFoundException(NotFoundException):
    code = "PRODUCT_NOT_FOUND"
    message = _("product not found.")


def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = PermissionDenied()
    elif isinstance(exc, ValidationError):
        exc = InvalidInputException(errors=exc.detail)
    elif isinstance(exc, MethodNotAllowed):
        exc = MethodNotAllowedException()
    elif isinstance(exc, NotFound):
        code = "NOT_FOUND"

    # Make sure were always working with an APIException or BaseStyleIconException
    if not isinstance(exc, (APIException, BaseException)):
        raise exc

    code = getattr(exc, "code", "")
    message = getattr(exc, "message", "")
    error_details = getattr(exc, "error_details", [])

    data = dict(message=message, error_details=error_details, code=code)

    return Response(data, status=exc.status_code)
