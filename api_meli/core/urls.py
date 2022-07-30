from django.urls import path
from .views import auth

from . import views

urlpatterns = [
  
    path('search-in-doc/', views.SearchInDoc.as_view(), name='search-in-doc'),
    path('list-drive/', views.ListDrive.as_view(), name='list-drive'),
    path('create-file/', views.CreateFile.as_view(), name='create-file'),
    path('delete-file/', views.DeleteFile.as_view(), name='delete-file'),
    path("v1/auth/login", auth.LoginView.as_view()),
    path("v1/auth/logout", auth.logout)
]
