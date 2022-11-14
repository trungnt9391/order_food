from email.policy import default
from enum import unique
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


"""
Database models
"""

from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
class  UserManager(BaseUserManager):
    """Manage for users."""
    def create_user(self, email, password= None, **extra_field):
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length= 255,unique = True)
    name = models.CharField(max_length =255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

