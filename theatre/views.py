from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from theatre.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)
from theatre.serializers import (
    GenreSerializer,
    GenreDetailSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
)


# class ImageUploadMixin:
#     @action(
#         methods=["POST"],
#         detail=True,
#         url_path="upload-image",
#         permission_classes=[IsAdminUser],
#     )
#     def upload_image(self, request, pk=None):
#         """Endpoint for uploading an image."""
#         obj = self.get_object()
#         serializer = self.get_serializer(obj, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GenreDetailSerializer

        return GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
