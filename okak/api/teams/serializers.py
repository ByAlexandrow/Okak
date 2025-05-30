from rest_framework import serializers

from api.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id'
        ]
        read_only_field = ['id']
