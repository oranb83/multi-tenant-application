from rest_framework.exceptions import APIException
from rest_framework import status


class DuplicatedExternalIdException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'Unprocessable Entity.'
    default_code = 'unprocessable_entity'
