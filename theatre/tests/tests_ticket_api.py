from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from theatre.models import Ticket
from theatre.serializers import TicketSerializer

from theatre.tests.config_for_tests import (
    create_sample_performance,
    create_sample_reservation
)


class AuthenticatedUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com",
            password="test123",
        )
        self.client.force_authenticate(self.user)

    def test_ticket_list(self):
        self.user.is_staff = True
        Ticket.objects.create(
            row=1,
            seat=1,
            performance=create_sample_performance(),
            reservation=create_sample_reservation(),
        )

        url = reverse("theatre:ticket-list")
        response = self.client.get(url)

        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_ticket_detail(self):
        self.user.is_staff = True
        ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=create_sample_performance(),
            reservation=create_sample_reservation(),
        )
        url = reverse("theatre:ticket-detail", args=[ticket.id])

        response = self.client.get(url)

        serializer = TicketSerializer(ticket)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_ticket_create_forbidden(self):
        payload = {
            "row": 10,
            "seat": 5,
        }
        url = reverse("theatre:ticket-list")
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_delete_forbidden(self):
        ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=create_sample_performance(),
            reservation=create_sample_reservation(),
        )
        url = reverse("theatre:ticket-detail", kwargs={"pk": ticket.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_create_ticket_allow(self):

        performance = create_sample_performance()
        reservation = create_sample_reservation()

        self.user.is_staff = True
        self.user.save()

        payload = {
            "row": 1,
            "seat": 1,
            "performance": performance.id,
            "reservation": reservation.id,
        }
        url = reverse("theatre:ticket-list")

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        ticket = Ticket.objects.first()
        self.assertEqual(ticket.row, 1)
        self.assertEqual(ticket.seat, 1)
        self.assertEqual(ticket.performance.id, performance.id)
        self.assertEqual(ticket.reservation.id, reservation.id)

    def test_admin_delete_ticket_allow(self):
        self.user.is_staff = True
        ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=create_sample_performance(),
            reservation=create_sample_reservation()
        )
        url = reverse("theatre:ticket-detail", kwargs={"pk": ticket.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
