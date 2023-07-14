from django.contrib import admin
from django.urls import path
from user.views import admin_signup, admin_signup_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsignup/', admin_signup, name='admin_signup'),
    path('adminsignup/success/', admin_signup_success, name='admin_signup_success'),
]
