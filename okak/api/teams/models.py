from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Team(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Направление команды',
    )
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
    # groups = models.ManyToManyField(
    #     Group,
    #     blank=True,
    #     related_name='worker_set',
    #     verbose_name='Группы',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     blank=True,
    #     related_name='worker_permissions',
    #     verbose_name='Разрешения',
    # )

    def __str__(self):
        return self.get_full_name() or self.username
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
