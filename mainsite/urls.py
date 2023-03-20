from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.mainpage, name='main'),
]