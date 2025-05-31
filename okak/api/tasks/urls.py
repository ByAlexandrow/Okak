from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import TaskViewSet, TaskStatusViewSet, WorkDirectionViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'task-statuses', TaskStatusViewSet, basename='task-statuses')
router.register(r'work-directions', WorkDirectionViewSet, basename='work-directions')

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
