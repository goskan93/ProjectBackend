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
    Website = models.CharField(max_length=120, blank=True, default="")
    Youtube = models.CharField(max_length=120, blank=True, default="")
    Instagram = models.CharField(max_length=120, blank=True, default="")
    Facebook = models.CharField(max_length=120, blank=True, default="")
    About = models.TextField(blank=True, default="", max_length=500)
    flaTravelWithChildren = models.BooleanField(default=False)
    flaTravelWithAnimals = models.BooleanField(default=False)
    flaOrganizeTrips = models.BooleanField(default=False)
    # Photo = models.TextField(blank=True, default="")
    Countries = models.ManyToManyField(Country)
    Languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.Name
