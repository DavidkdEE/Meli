from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
from rest_framework import status

class ConectedFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('An error occurred while trying to connect to the Google DRIVE API.')
    default_code = 'Failed to connect to DRIVE'

class WordNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('The word is not found in the text.')
    default_code = 'Word not found'