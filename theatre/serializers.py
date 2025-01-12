from rest_framework import serializers

from theatre.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    Reservation,
    Performance,
    Ticket,
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "photo",
        )


class GenreSerializer(serializers.ModelSerializer):
    plays = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Play.objects.all()
    )

    class Meta:
        model = Genre
        fields = ("id", "name", "plays")


class PlaySerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "actors",
            "genres",
            "poster",
        )


class GenreDetailSerializer(GenreSerializer):
    plays = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Play.objects.all()
    )

    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ("plays",)

    def get_plays(self, obj):
        return [play.title for play in obj.plays.all()]


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row")


class PerformanceSerializer(serializers.ModelSerializer):
    play = serializers.StringRelatedField()
    theatre_hall = serializers.StringRelatedField()

    class Meta:
        model = Performance
        fields = ("id", "play", "theatre_hall", "show_time")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance", "reservation")
