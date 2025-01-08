from django.contrib import admin

from theatre.models import (
    Play,
    Actor,
    TheatreHall,
    Genre,
    Ticket,
    Reservation,
    Performance
)

admin.site.register(Play)
admin.site.register(Performance)
admin.site.register(Actor)
admin.site.register(TheatreHall)
admin.site.register(Genre)
admin.site.register(Ticket)
admin.site.register(Reservation)
