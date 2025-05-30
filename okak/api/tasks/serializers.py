from rest_framework import serializers

from api.tasks.models import Task, TaskStatus, WorkDirection


class TaskStatus(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id']
        read_only_field = ['id']


class WorkDirection(serializers.ModelSerializer):
    class Meta:
        model = WorkDirection
        fields = ['id']
        read_only_field = ['id']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']
        read_only_field = ['id', 'created_at']
