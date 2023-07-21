from django.contrib import admin
from django.urls import path
from .views import create_post

urlpatterns = [
    path('newpost/', create_post, name='create_post'),
]
