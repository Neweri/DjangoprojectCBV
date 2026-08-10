from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('admin')
    MODERATOR = 'moderator', _('moderator')
    USER = 'user', _('user')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    first_name = models.CharField(max_length=150, verbose_name='first name', default='Anonymous')
    last_name = models.CharField(max_length=150, verbose_name='last name', default='Anonymous')
    avatar = models.ImageField(upload_to='users/media', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='telegram username', **NULLABLE)
    max_messenger = models.CharField(max_length=150, verbose_name='Аккаунт MAX', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}\n{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
        # abstract = True - модель будет базовым абстрактным классом
        # app_label = 'my_app' - указание на приложение к которому модель принадлежит
        # base_manager_name  = 'objects'
        # db_table = 'users_user' # имя таблицы в БД
