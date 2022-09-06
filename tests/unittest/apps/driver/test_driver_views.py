from django.test import TestCase
from rest_framework import status


class DriverViewTestCase(TestCase):
    def test_driver_status_code_200(self):
        response = self.client.get("http://127.0.0.1:8000/drivers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
