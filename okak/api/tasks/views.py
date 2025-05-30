from rest_framework import viewsets

from api.tasks.models import Task
from api.tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    quesryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
