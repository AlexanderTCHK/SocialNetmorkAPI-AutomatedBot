from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
