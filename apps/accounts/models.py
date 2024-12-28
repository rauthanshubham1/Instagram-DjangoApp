from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=128)
    profile_picture = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(
        'self',
        related_name='followingg',
        symmetrical=False,
        blank=True
    )

    following = models.ManyToManyField(
        'self',
        related_name='followerss',
        symmetrical=False,
        blank=True
    )
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username}'s profile"
