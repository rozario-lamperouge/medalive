from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, MediaViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'medias', MediaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]