from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from theatre.models import Actor
from theatre.serializers import  ActorSerializer


class AuthenticatedUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser",
            password="test123",
        )
        self.client.force_authenticate(self.user)



    def test_actor_retrieve(self):
        actor = Actor.objects.create(
            first_name="Jason",
            last_name="Statham",
        )

        url = reverse("theatre:actor-detail", args=[actor.id])
        response = self.client.get(url)

        serializer = ActorSerializer(actor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_actor_create_forbidden(self):
        payload = {
            "first_name": "test name",
            "last_name": "test last name",
        }
        url = reverse("theatre:actor-list")
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_actor_delete_forbidden(self):
        actor = Actor.objects.create(
            first_name="Jason",
            last_name="Statham",
        )
        url = reverse("theatre:actor-detail", kwargs={"pk": actor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_actor_create_allow(self):
        self.user.is_staff = True
        payload = {
            "first_name": "Jason",
            "last_name": "Statham",
        }
        url = reverse("theatre:actor-list")
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_delete_allow(self):
        self.user.is_staff = True
        actor = Actor.objects.create(
            first_name="Jason",
            last_name="Statham",
        )
        url = reverse("theatre:actor-detail", kwargs={"pk": actor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
