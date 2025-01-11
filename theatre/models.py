import pathlib
import uuid

from django.conf import settings
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser


def actor_photo_path(instance: "Actor", filename: str) -> pathlib.Path:
    extension = pathlib.Path(filename).suffix
    filename = f"{slugify(instance.last_name)}-{uuid.uuid4()}" + extension
    return pathlib.Path("uploads/actors/") / pathlib.Path(filename)

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to=actor_photo_path)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def poster_path(instance: "Play", filename: str) -> pathlib.Path:
    extension = pathlib.Path(filename).suffix
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}" + extension
    return pathlib.Path("uploads/posters/") / pathlib.Path(filename)

class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(null=True, blank=True, upload_to=poster_path)

    def __str__(self):
        return self.title


class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(
        Play,
        on_delete=models.CASCADE,
    )
    theatre_hall = models.ForeignKey(
        TheatreHall,
        on_delete=models.CASCADE,
        related_name="performances",
    )
    show_time = models.DateTimeField()

    def __str__(self):
        return self.play.title


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    rows = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    def __str__(self):
        return self.performance.play
