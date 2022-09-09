import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ShippingViewTestCase(TestCase):
    def test_shipping_status_code_200(self):
        response = self.client.get("http://127.0.0.1:8000/shipping/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shipping_create(self):
        data = json.dumps(
            {
                "origin": {
                    "street": "Rua José Leopoldo Lima",
                    "number": "1064",
                    "complement": "Casa",
                    "neighborhood": "Santa Maria da Vitória",
                    "city": "Santa Maria da Vitória",
                    "reference": "Barbearia",
                    "state": "BA",
                    "zip_code": "47640000",
                },
                "destination": {
                    "street": "Rua Sabino Pedro",
                    "number": "16",
                    "complement": "Restaurante",
                    "neighborhood": "Laranjeiras",
                    "city": "Balneário Camboriú",
                    "reference": "Escola Edir",
                    "state": "SC",
                    "zip_code": "88333425",
                },
            }
        )
        client = APIClient()
        response = client.post(
            "http://127.0.0.1:8000/shipping/",
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["origin"]["street"], "Rua José Leopoldo Lima")
        self.assertEqual(response.data["destination"]["street"], "Rua Sabino Pedro")
