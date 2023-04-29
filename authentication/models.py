import os.path
from uuid import uuid4

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


def upload(instance, filename):
    return "/".join([f"employee/resume", f"{str(uuid4())}{os.path.splitext(filename)[1]}"])


class UserManager(BaseUserManager):
    """
    Custom user with unique email
    """

    def create_user(self, username, email, password):
        # Overrides the django create user method, creates custom user when called
        if username is None:
            raise TypeError("No username provided")
        if email is None:
            raise TypeError("No email provided")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        # Overrides the django create super user method, creates cutom superuser when called
        if password is None:
            raise TypeError("No password provided")
        if email is None:
            raise TypeError("No email provided")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user 
    """

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.username

