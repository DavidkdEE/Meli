from django.urls import path
from .views import auth

from . import views

urlpatterns = [
  
    path('search-in-doc/<str:id>', views.SearchInDoc.as_view(), name='search-in-doc'),
    path('files', views.ListFilesView.as_view(), name='files'),
    path('files/<str:id>', views.DeleteFile.as_view(), name='delete-file'),
    path("v1/auth/login", auth.LoginView.as_view()),
    path("v1/auth/logout", auth.logout)
]
