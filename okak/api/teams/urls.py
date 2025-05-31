from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, WorkerViewSet


router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'workers', WorkerViewSet, basename='workers')

urlpatterns = [
    path('', include(router.urls)),
]
