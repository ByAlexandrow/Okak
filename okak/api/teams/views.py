from rest_framework import viewsets

from api.teams.models import Team
from api.teams.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
