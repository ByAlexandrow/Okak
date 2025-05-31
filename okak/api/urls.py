from django.urls import path, include

urlpatterns = [
    path('tasks/', include('api.tasks.urls')),
    path('teams/', include('api.teams.urls')),
]
