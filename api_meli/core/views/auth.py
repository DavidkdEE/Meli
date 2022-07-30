from django.utils.translation import gettext_lazy as _

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, authenticate,
    login as django_login, logout as django_logout
)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import exceptions, serializers

from rest_framework.decorators import (
    api_view,
    permission_classes,
)

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

UserModel = get_user_model()

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)
       

class CredsSerializer(serializers.Serializer):
    username_field = UserModel.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)
        if self.user is None:
            raise exceptions.AuthenticationFailed
        return {}


class LoginView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = CredsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        django_login(self.request, serializer.user)
        return Response(UserSerializer(request.user).data)

@api_view(["POST"])
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout(request: Request) -> Response:
    django_logout(request)
    return Response({})
