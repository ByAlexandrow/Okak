from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TaskStatusViewSet, WorkDirectionViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'statuses', TaskStatusViewSet, basename='statuses')
router.register(r'workers', WorkDirectionViewSet, basename='workers')

urlpatterns = [
    path('', include(router.urls)),
]
