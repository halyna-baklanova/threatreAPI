from datetime import datetime

from rest_framework.reverse import reverse

from theatre.models import Play, Performance, TheatreHall, Reservation
from user.models import User


BASE_URL = reverse("theatre:play-list")
DETAIL_URL = reverse("theatre:play-detail", kwargs={"pk": 1})


def create_sample_theatre(**kwargs) -> TheatreHall:
    defaults = {
        "name": "Test Theatre",
        "rows": 30,
        "seats_in_row": 30,
    }
    defaults.update(kwargs)
    return TheatreHall.objects.create(**defaults)


def create_sample_plays(**kwargs) -> Play:
    defaults = {
        "title": "Test Play",
        "description": "Test Play",
    }
    defaults.update(kwargs)
    return Play.objects.create(**defaults)


def create_sample_performance(**kwargs) -> Performance:
    defaults = {
        "play": create_sample_plays(),
        "show_time": datetime.now(),
        "theatre_hall": create_sample_theatre(),
    }
    defaults.update(kwargs)
    return Performance.objects.create(**defaults)


def create_sample_reservation(**kwargs) -> Reservation:
    defaults = {
        "created_at": datetime.now(),
        "user": User.objects.create_user(
            email="testuser",
            password="test-1-2-3"
        ),
    }
    defaults.update(kwargs)
    return Reservation.objects.create(**defaults)
