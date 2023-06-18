from django.contrib.auth.models import (
    User
)
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Username {self.user.username}"
