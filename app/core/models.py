"""
Test models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    """
    email : must be unique
    is_active : default is active but can be switched off to false as well
    is_staff : used to login to Django admin panel
    """

    USERNAME_FIELD = 'email'
    """
    A string describing the name of the field on the user model that is used
    as the unique identifier. This will usually be a username of some kind,
    but it can also be an email address, or any other unique identifier.
    The field must be unique (e.g. have unique=True set in its definition),
    unless you use a custom authentication backend that can support non-unique
    usernames.


    class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)

    USERNAME_FIELD = 'identifier'
    """
