from django.urls import path
from .views import auth

from . import views

urlpatterns = [
    path('files/<str:id>/search-in-doc', views.SearchInDoc.as_view(), name='search-in-doc'),
    path('files', views.ListFilesView.as_view(), name='files'),
    path('files/<str:id>', views.DeleteFile.as_view(), name='delete-file'),
    path("auth/login", auth.LoginView.as_view()),
    path("auth/logout", auth.logout)
]
