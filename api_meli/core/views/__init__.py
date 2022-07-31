from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api_google.credentials import GoogleDrive
from core.services.file_service import FileService


param_word = openapi.Parameter('word', openapi.IN_QUERY, description="word", type=openapi.TYPE_STRING)

param_title = openapi.Parameter('title', openapi.IN_QUERY, description="title", type=openapi.TYPE_STRING)
param_description = openapi.Parameter('description', openapi.IN_QUERY, description="description", type=openapi.TYPE_STRING)

field_enum = [
    'id_document',
    'word',
    'title',
    'description'
]
creds = GoogleDrive().get_credentials()

class SearchInDoc(APIView):
    """Busca una palabra en un documento"""
    @swagger_auto_schema(
        manual_parameters=
            [param_word])

    def get(self, request, id, format=None):
        word = request.query_params.get('word')
        search_word = FileService().search_word(id, word)
        return Response(search_word, status=status.HTTP_200_OK)

class ListFilesView(APIView):
    """Lista los archivos almacenados en Google Drive"""
    
    def get(self, request, format=None):
        files = FileService().get_files()
        return Response(files, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        manual_parameters=
        [param_title, param_description])
    def post(self, request, format=None):
        title = request.query_params.get('title')
        description = request.query_params.get('description')
        create_file = FileService().create_file(title, description)
        return Response(create_file, status=status.HTTP_200_OK)
        
# class CreateFile(APIView):
#     """Crea un archivo de Google Drive a partir de los parametros de titulo y descripción"""
#     @swagger_auto_schema(
#         manual_parameters=
#             [param_title, param_description])

#     def post(self, request, format=None):
#         title = request.query_params.get('title')
#         description = request.query_params.get('description')
#         create_file = FileService().create_file(title, description)
#         return Response(create_file, status=status.HTTP_200_OK)

class DeleteFile(APIView):
    """Elimina un archivo de Google Drive a partir de su ID"""

    def delete(self, request, id, format=None):
        delete_file = FileService().delete_file(id)
        return Response(delete_file, status=status.HTTP_204_NO_CONTENT)
