from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.services.file_service import FileService


param_word = openapi.Parameter('word', openapi.IN_QUERY, description="Word to search", type=openapi.TYPE_STRING)


class SearchInDoc(APIView):
    """Search for a word in a document"""
    @swagger_auto_schema(
        manual_parameters=[param_word])
    def get(self, request, id, format=None):
        word = request.query_params.get('word')
        search_word = FileService().search_word(id, word)
        return Response(search_word, status=status.HTTP_200_OK)


class ListFilesView(APIView):
    """List the files stored in Google Drive"""

    def get(self, request, format=None):
        files = FileService().get_files()
        return Response(files, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of document'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of document'),
        }))
    def post(self, request, format=None):
        title = request.data.get('title')
        description = request.data.get('description')
        create_file = FileService().create_file(title, description)
        return Response(create_file, status=status.HTTP_200_OK)


class DeleteFile(APIView):
    """Delete a file from Google Drive based on its ID"""

    def delete(self, request, id, format=None):
        delete_file = FileService().delete_file(id)
        return Response(delete_file, status=status.HTTP_204_NO_CONTENT)
