from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from api.apps.core.models import BaseModel  # Assuming you have a BaseModel defined


class UserAccountManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, phone_number, and password.
        """
        if not username:
            raise ValueError('The Username must be set')
        if not phone_number:
            raise ValueError('The Phone Number must be set')

        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(username, password=password, **extra_fields)


class User(BaseModel, AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
