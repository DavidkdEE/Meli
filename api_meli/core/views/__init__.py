import logging
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from httplib2 import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from googleapiclient.errors import HttpError
from core.exceptions import ConectedFailed

from api_google.credentials import GoogleDrive

from googleapiclient.discovery import build
# logger = logging.getLogger(__name__)



param_id_document = openapi.Parameter('id_document', openapi.IN_QUERY, description="id_document", type=openapi.TYPE_STRING)
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
            [param_id_document, param_word])

    def get(self, request, format=None):
        try:
            id_document = request.query_params.get('id_document')
            word = request.query_params.get('word')
            service = build('docs', 'v1', credentials=creds)
            doc = service.documents().get(documentId=id_document).execute()
            doc_content = doc.get('body').get('content')
            text = []
            for paragraph in doc_content:
                if paragraph.get('paragraph'):
                    content = paragraph.get('paragraph').get('elements')[0].get('textRun').get('content')
                    list_word = content.split(' ')
                    for _word in list_word:
                        if _word == '\n':
                            continue
                        __word = _word.rstrip()
                        text.append(__word.lower())
            if word.lower() in text:
                return Response('Palabra se encuentra en el texto',status=status.HTTP_200_OK)
            else:
                return Response('Palabra NO se encuentra en el texto',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except HttpError as err:
            # logger.error(f"Se produjo un error al buscar contenido del documento. {str(err)}")
            raise ConectedFailed(err)


class ListFilesView(APIView):
    """Lista los archivos almacenados en Google Drive"""
    
    def get(self, request, format=None):
        try:
            service = build('drive', 'v3', credentials=creds)
            results = service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            if not items:
                print('No files found.')
                return
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
            return Response(items, status=status.HTTP_200_OK)
        except HttpError as err:
            # logger.error(f"Se produjo un error al listar contenido del DRIVE. {str(err)}")
            return Response(err.content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateFile(APIView):
    """Crea un archivo de Google Drive a partir de los parametros de titulo y descripción"""
    @swagger_auto_schema(
        manual_parameters=
            [param_title, param_description])

    def post(self, request, format=None):
        try:
            title = request.query_params.get('title')
            description = request.query_params.get('description')
            
            if title is None or description is None:
                title = request.data.get('title')
                description = request.data.get('description')

            service = build('docs', 'v1', credentials=creds)
            doc = {
                'title': title,
            }
            response = service.documents().create(body=doc).execute()
            id_document = response.get('documentId')
            requests=[
                {
                    "insertText": {
                        "text": description,
                        "location": {
                            "index": 1
                        }
                    }
                }
            ]
            print('File ID: %s' % response.get('id'))
            result = service.documents().batchUpdate(documentId=id_document, body={'requests': requests}).execute()
            data = {
                'id': id_document,
                'titulo': title,
                'descripcion': description
            }
            return Response(data, status=status.HTTP_200_OK)
        except HttpError as err:
            # logger.error(f"Se produjo un error al crear un doc en el DRIVE. {str(err)}")
            return Response(err.content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteFile(APIView):
    """Elimina un archivo de Google Drive a partir de su ID"""
    @swagger_auto_schema(
        manual_parameters=
            [param_id_document])

    def get(self, request, format=None):
        try:
            id_document = request.query_params.get('id_document')
            service = build('drive', 'v3', credentials=creds)
            service.files().delete(fileId=id_document).execute()
            return Response('Archivo eliminado con exito',status=status.HTTP_204_NO_CONTENT)

        except HttpError as err:
            return Response(err.content, status=status.HTTP_404_NOT_FOUND)