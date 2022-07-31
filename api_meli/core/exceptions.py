from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
from rest_framework import status

class ConectedFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('se produjo un error al intentar conectar con la API de Google DRIVE.')
    default_code = 'Error al conectar con DRIVE'

class WordNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('La palabra no se encuentra en el texto.')
    default_code = 'Palabra no encontrada'