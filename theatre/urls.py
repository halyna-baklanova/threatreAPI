from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    GenreViewSet,
    ActorViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)

router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)
router.register("theatre_halls", TheatreHallViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
