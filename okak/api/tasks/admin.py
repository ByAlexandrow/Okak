from django.contrib import admin

from api.tasks.models import TaskStatus, WorkDirection, Task


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_preview', 'is_published')


@admin.register(WorkDirection)
class WorkDirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'deadline', 'status')
