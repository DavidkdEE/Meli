from faker import Faker
from django.test import Client
from django.urls import reverse

from core.serializers import User

fake = Faker()
client = Client()


def make_valid_user(
    email: str = fake.email(),
    username: str = fake.email(),
    password: str = fake.password(),
    is_active: bool = True,
    is_superuser: bool = True,
) -> User:
    user = User.objects.create(
        email=email,
        username=username,
    )
    user.set_password(password)
    user.is_active = is_active
    user.is_superuser = is_superuser
    user.save()
    token = make_get_token(username, password)
    return user, token


def make_get_token(
    username: str,
    password: str
):
    payload = {
        "username": username,
        "password": password,
    }
    response = client.post(reverse('token_obtain_pair'), payload, content_type='application/json')
    dict_response = response.data
    resp = ''
    for key, value in dict_response.items():
        if key == 'access':
            resp = value
    return resp
