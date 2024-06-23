from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    В коде, UserManager не используется напрямую, но он указан в классе User как objects.
    Это означает, что UserManager используется для управления объектами класса User в Django.
    Он тут не ипользуется на прямую, но отвечает за удаление, добовление объектов класса User
    """
    # Указание что этот менджер должен быть использован в миграциях джанго
    use_in_migrations = True

    # Создание пользователя и вывод исключения в терминал
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('У пользователя должен быть email')
        email = self.normalize_email(email)  # Нормализует данные, переводит в нижний регистор, удаляет пробелы и т.д
        user = self.model(email=email, **extra_fields)  # Ссылка на модель, передача email и других полей (extra_fields)
        user.set_password(password)  # Устонавливает пароль
        user.save(using=self._db)  # Сохроняет пользователя в бд
        return user

    # Создание супер пользователя
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=40, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Authorized user'
        verbose_name_plural = 'Authorized users'
