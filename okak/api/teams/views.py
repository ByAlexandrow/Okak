from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.teams.models import Team, Worker
from api.teams.serializers import TeamSerializer, WorkerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
