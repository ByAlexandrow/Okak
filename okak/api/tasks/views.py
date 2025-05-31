from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from api.tasks.models import Task, TaskStatus, WorkDirection
from api.tasks.serializers import TaskSerializer, TaskStatusSerializer, WorkDirectionSerializer
from api.tasks.permissions import IsManagerOrReadOnlyStatus


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkDirectionViewSet(viewsets.ModelViewSet):
    queryset = WorkDirection.objects.all()
    serializer_class = WorkDirectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskViewSet(viewsets.ModelViewSet):
    quesryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsManagerOrReadOnlyStatus]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def create(self, request, *args, **kwargs):
        if request.user.team.title.lower() != 'Менеджер':
            return Response({
                'detail': 'Создавать задачи может только менеджер'
            }, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if request.user.team.title.lower() != 'Менеджер':
            return Response({
                'detail': 'Удалять задачи может только менеджер.'
            }, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
