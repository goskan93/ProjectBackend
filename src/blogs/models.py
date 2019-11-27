from django.db import models
import uuid
from django.utils.timezone import now
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# TODO: user have id uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    BlogId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    DataCreated = models.DateField(
        editable=False, auto_now=False, auto_now_add=True)
    DataUpdated = models.DateField(auto_now=True, auto_now_add=False)
    UserId = models.ForeignKey(
        User, on_delete=models.CASCADE, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=120, default="")
    # website = models.CharField(max_length=120, blank=True, default="")
    # youtube = models.CharField(max_length=120, blank=True, default="")
    # instagram = models.CharField(max_length=120, blank=True, default="")
    # facebook = models.CharField(max_length=120, blank=True, default="")
    # Countries = models.ManyToManyField(Country)
    # Languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.Name
