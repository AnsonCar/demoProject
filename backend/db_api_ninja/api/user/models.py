import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from ninja import Schema

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class UserIn(Schema):
    username: str
    password: str

class UserOut(Schema):
    id: int
    uuid: uuid.UUID
    username: str
    email: str
