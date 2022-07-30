from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from faker import Faker
from tests.shemas import CreateFileResponse
from tests.shemas import ListFilesResponse


from tests.utils import make_valid_user
fake = Faker()

class ApiTest(TestCase):
    client = Client()
    def setUp(self):
        self.user, self.token = make_valid_user(is_active=True)

    def test_create_doc(self):
        """Creation doc test"""
        
        payload = {
            "title": fake.name(),
            "description": fake.text(),
        }
        authorization = 'Bearer ' + self.token
        response = self.client.post(
            reverse('create-file'),
            data=payload,
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.data:
            CreateFileResponse(**response.data)
        self.assertEqual(response.data.get('titulo'), payload.get('title'))
        self.assertEqual(response.data.get('descripcion'), payload.get('description'))

        response = self.client.get(
            reverse('delete-file'),
            data={'id_document': response.data.get('id')},
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_get_list_doc(self):
        """Creation get list test"""
        authorization = 'Bearer ' + self.token
        response = self.client.get(
            reverse('list-drive'),
            HTTP_AUTHORIZATION=authorization,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.data:
            for file in response.data:
                ListFilesResponse(**file)

    def test_get_list_doc_no_autenticated(self):
        """Creation get list test"""
        response = self.client.get(
            reverse('list-drive'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
