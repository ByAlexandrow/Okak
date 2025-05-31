from django.contrib import admin

from api.teams.models import Team, Worker


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'team', 'tech_stack')

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'Full name'
