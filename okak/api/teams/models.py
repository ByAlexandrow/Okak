from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Направление команды',
    )
    # description = models.CharField(
    #     max_length=150,
    #     null=False,
    #     blank=False,
    #     verbose_name='Описание',
    # )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Worker(AbstractUser):
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='workers',
        verbose_name='Команда',
    )
    tech_stack = models.TextField(
        blank=False,
        help_text='Перечислите здесь стек технологий',
        verbose_name='Стек технологий',
    )

    def __str__(self):
        return self.get_full_name() or self.username
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
