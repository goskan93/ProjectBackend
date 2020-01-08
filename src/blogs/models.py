from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
import uuid

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
    blogId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    dataCreated = models.DateField(
        editable=False, auto_now=False, auto_now_add=True)
    dataUpdated = models.DateField(auto_now=True, auto_now_add=False)
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, default="")
    website = models.CharField(max_length=120, blank=True, default="")
    youtube = models.CharField(max_length=120, blank=True, default="")
    instagram = models.CharField(max_length=120, blank=True, default="")
    facebook = models.CharField(max_length=120, blank=True, default="")
    about = models.TextField(blank=True, default="", max_length=500)
    flaTravelWithChildren = models.BooleanField(default=False)
    flaTravelWithAnimals = models.BooleanField(default=False)
    flaOrganizeTrips = models.BooleanField(default=False)
    # Photo = models.TextField(blank=True, default="")
    countries = models.ManyToManyField(Country)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
