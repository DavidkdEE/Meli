from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
from rest_framework import status

class ConectedFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('se produjo un error al intentar conectar con la API de Google DRIVE.')
    default_code = 'Error al conectar con DRIVE'
