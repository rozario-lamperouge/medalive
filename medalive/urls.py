from django.contrib import admin
from django.urls import path
from user.views import admin_signup, admin_signup_success
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsignup/', admin_signup, name='admin_signup'),
    path('adminsignup/success/', admin_signup_success, name='admin_signup_success'),
    path('doctor/', include('doctor.urls')),
    path('', include('user.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
