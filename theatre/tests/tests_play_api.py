from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from theatre.models import Play, Actor, Genre
from theatre.serializers import PlaySerializer
from theatre.tests.config_for_tests import create_sample_plays, create_sample_performance, create_sample_theatre

BASE_URL = reverse("theatre:play-list")

class AuthenticatedUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com",
            password="test123",
        )
        self.client.force_authenticate(self.user)

    def test_play_list(self):
        create_sample_plays()
        response = self.client.get(BASE_URL)

        plays = Play.objects.all()
        serializer = PlaySerializer(
            plays,
            many=True
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data,
            serializer.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data,
            serializer.data
        )

    def test_play_create_forbidden(self):
        payload = {
            "title": "test play",
            "description": "test play",
        }
        response = self.client.post(
            BASE_URL,
            payload
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_play_delete_forbidden(self):
        play = create_sample_plays()
        url = reverse(
            "theatre:play-detail",
            kwargs={"pk": play.pk}
        )
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_admin_play_create_allow(self):
        self.user.is_staff = True
        payload = {
            "title": "test play",
            "description": "test play",
        }

        url = reverse("theatre:play-list")

        response = self.client.post(url, payload)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_admin_play_delete_allow(self):
        self.user.is_staff = True
        play = create_sample_plays()
        url = reverse(
            "theatre:play-detail",
            kwargs={"pk": play.pk}
        )
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
