from django.test import TestCase
from apps.shipping.models import Shipping, Origin, Destination


class OriginModelTestCase(TestCase):

    def setUp(self):
        Origin.objects.create(
            street="Rua José Leopoldo Lima",
            number="1064",
            complement="Casa",
            neighborhood="Santa Maria da Vitória",
            city="Santa Maria da Vitória",
            reference="Barbearua",
            state="BA",
            zip_code="47640000"
        )

    def test_return_str(self):
        origin = Origin.objects.get(id=1)
        expected_object_name = f"{origin.street} - {origin.city}"
        self.assertEqual(origin.__str__(), expected_object_name)


class DestinationModelTestCase(TestCase):

    def setUp(self):
        Destination.objects.create(
            street="Rua Sabino Pedro",
            number="16",
            complement="Restaurante",
            neighborhood="Laranjeiras",
            city="Balneário Camboriú",
            reference="Escola Edir",
            state="SC",
            zip_code="88333425"
        )

    def test_return_str(self):
        destination = Destination.objects.get(id=1)
        expected_object_name = f"{destination.street} - {destination.city}"
        self.assertEqual(destination.__str__(), expected_object_name)

