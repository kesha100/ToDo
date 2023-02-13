from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .managers import MyUserManager

# Create your models here.


class MyUser(AbstractBaseUser):
    username = None
    email = models.EmailField(
        unique=True,
        max_length=255
    )
    image = models.ImageField(upload_to='', default=None, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email