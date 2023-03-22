from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.mainpage, name='main'),
    path("news/", views.NewsView.as_view(), name='news'),
    path("news/<slug:slug>/", views.NewsDetail.as_view(), name='news_details')
]
