from rest_framework import serializers

from api.teams.models import Team, Worker


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'title', 'is_published']
        read_only_field = ['id']


class WorkerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True
    )

    class Meta:
        model = Worker
        fields = [
            'id', 'username', 'first_name', 'last_name',
            'email', 'team', 'team_id', 'tech_stack'
        ]
        read_only_field = ['id']
