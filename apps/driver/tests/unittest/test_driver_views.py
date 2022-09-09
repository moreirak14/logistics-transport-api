import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class DriverViewTestCase(TestCase):
    def test_driver_status_code_200(self):
        response = self.client.get("http://127.0.0.1:8000/drivers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_create(self):
        data = json.dumps(
            {
                "first_name": "José",
                "last_name": "Sei lá",
                "age": 52,
                "gender": "M",
                "own_vehicle": True,
                "driver_license": "D-E",
                "loaded": False,
                "vehicle_types": "5",
            }
        )
        client = APIClient()
        response = client.post(
            "http://127.0.0.1:8000/drivers/", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "José")
