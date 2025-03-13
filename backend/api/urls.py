# api/urls.py
from django.urls import path
from .views import prueba_api

urlpatterns = [
    path("test/", prueba_api, name="test_api"),
]
