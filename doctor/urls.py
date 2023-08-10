from django.contrib import admin
from django.urls import path
from .views import create_post, loginView, homeView, LoginView, LogoutView, CreatePostAPIView

urlpatterns = [
    path('', homeView, name='home'),
    path('newpost/', create_post, name='create_post'),
    path('login/', loginView, name='login'),
    path('api/login/', LoginView.as_view(), name='login-api'),
    path('api/logout/', LogoutView.as_view(), name='logout-api'),
    path('api/createpost/', CreatePostAPIView.as_view(), name='createpost-api'),
]
