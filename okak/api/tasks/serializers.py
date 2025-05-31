from rest_framework import serializers

from api.tasks.models import Task, TaskStatus, WorkDirection
from api.teams.models import Team
from api.teams.serializers import TeamSerializer


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id', 'title', 'color_tag', 'is_published']
        read_only_field = ['id']


class WorkDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDirection
        fields = ['id', 'title', 'is_published']
        read_only_field = ['id']


class TaskSerializer(serializers.ModelSerializer):
    direction = WorkDirectionSerializer(read_only=True)
    direction_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkDirection.objects.all(), source='direction', write_only=True
    )
    status = TaskStatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=TaskStatus.objects.all(), source='status', write_only=True
    )
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'direction', 'direction_id',
            'deadline', 'status', 'status_id', 'team', 'team_id', 'created_at'
        ]
        read_only_field = ['id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            if user.team.title.lower() != 'Менеджер':
                for field_name in self.fields:
                    if field_name != 'status':
                        self.fields[field_name].read_only = True
        else:
            for field in self.fields.values():
                field.read_only = True
    
    def validate_deadline(self, value):
        from django.utils import timezone
        if value < timezone.localdate():
            raise serializers.ValidationError(
                'Дедлайн не может быть в прошлом!'
            )
        return value
