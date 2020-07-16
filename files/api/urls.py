from .views import DocumentViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('files', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls))
]