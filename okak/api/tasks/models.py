from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.core.exceptions import ValidationError

from api.teams.models import Team


class TaskStatus(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Статус выполнения задачи',
    )
    color_tag = models.CharField(
        max_length=7,
        verbose_name='Цветовой тэг (HEX)',
        help_text='Цвет в формате #000000',
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
    )

    def color_preview(self):
        if self.color_tag:
            return format_html(
                '<div style="width: 30px; height: 20px; background-color: {}; border: 1px solid #000;"></div>',
                self.color_tag
            )
        return "-"
    color_preview.short_description = 'Цвет'

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статус выполнения задачи'
        verbose_name_plural = 'Статусы выполнения задач'


class WorkDirection(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Направление',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'


class Task(models.Model):    
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Название задачи',
    )
    description = models.TextField(
        max_length=200,
        verbose_name='Описание задачи',
    )
    direction = models.OneToOneField(
        WorkDirection,
        on_delete=models.CASCADE,
        verbose_name='Направление работы',
    )
    deadline = models.DateField(
        verbose_name='Дедлайн',
    )
    status = models.OneToOneField(
        TaskStatus,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        verbose_name='Статус задачи',
    )
    team = models.OneToOneField(
        Team,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Команда',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def clean(self):
        super().clean()
        if self.deadline < timezone.localdate():
            raise ValidationError(
                {'dedline': 'Дедлайн не может быть в прошлом!'}
            ) 

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]
        ordering = ['-created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
