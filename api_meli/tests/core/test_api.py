from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from faker import Faker
from tests.shemas import CreateFileResponse
from tests.shemas import ListFilesResponse
from unittest.mock import patch


from tests.utils import make_valid_user
fake = Faker()

class ApiTest(TestCase):
    client = Client()
    def setUp(self):
        self.user, self.token = make_valid_user(is_active=True)

    def fake_create_file(self, title, google_creds) -> str:
        return "id_file"

    def fake_update_file(self, id_document, description, google_creds) -> dict:
        data = {
            'id': "id_file",
            'titulo': 'title',
            'descripcion': 'description'
        }
        return data
    
    def fake_list_files(self, google_creds) -> dict:
        data = [{
            'id': "id_file",
            'name': 'title',
        }]
        return data
    
    def fake_get_creds(self):
        return {}

    def fake_delete_file(self, file_id, google_creds) -> dict:
        return status.HTTP_204_NO_CONTENT

    @patch('api_google.google_drive.GoogleDriveService.create_file', fake_create_file)
    @patch('api_google.google_drive.GoogleDriveService.update_file', fake_update_file)
    @patch('api_google.credentials.GoogleDrive.get_credentials', fake_get_creds)
    def test_create_file(self):
        """Creation doc test"""
        payload = {
            "title": fake.name(),
            "description": fake.text(),
        }
        authorization = 'Bearer ' + self.token
        response = self.client.post(
            reverse('files'),
            data=payload,
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        CreateFileResponse(**response.data)
        self.assertEqual(response.data.get('id'), 'id_file')
        self.assertEqual(response.data.get('titulo'), payload.get('title'))
        self.assertEqual(response.data.get('descripcion'), payload.get('description'))

    def test_create_file_unauthorizated(self):
        """Creation doc unauthorizated test"""
        payload = {
            "title": fake.name(),
            "description": fake.text(),
        }
        response = self.client.post(
            reverse('files'),
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch('api_google.google_drive.GoogleDriveService.list_files', fake_list_files)
    @patch('api_google.credentials.GoogleDrive.get_credentials', fake_get_creds)
    def test_get_files(self):
        """Creation get list test"""
        authorization = 'Bearer ' + self.token
        response = self.client.get(
            reverse('files'),
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.data:
            for file in response.data:
                ListFilesResponse(**file)

    @patch('api_google.google_drive.GoogleDriveService.delete_file', fake_delete_file)
    @patch('api_google.credentials.GoogleDrive.get_credentials', fake_get_creds)
    def test_delete_file(self):
        """Creation get list test"""
        authorization = 'Bearer ' + self.token
        response = self.client.delete(
            reverse('delete-file', kwargs={'id': 'id_file'}),
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
