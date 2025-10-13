"""
Tests for the health check endpoint.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    """
    Tests for the health check endpoint.
    """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("health-check")

    def test_health_check(self):
        """
        Test that the health check endpoint returns a 200
        status code and the expected response.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"healthy": True})
