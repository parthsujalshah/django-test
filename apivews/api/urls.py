from django.urls import path, include
from .views import TempView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', TempView)

urlpatterns = [
    path('', include(router.urls)),
]