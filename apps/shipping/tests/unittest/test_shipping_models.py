from django.test import TestCase

from apps.shipping.models import Destination, Origin, Shipping


class OriginModelTestCase(TestCase):
    def setUp(self):
        Origin.objects.create(
            street="Rua José Leopoldo Lima",
            number="1064",
            complement="Casa",
            neighborhood="Santa Maria da Vitória",
            city="Santa Maria da Vitória",
            reference="Barbearia",
            state="BA",
            zip_code="47640000",
        )

    def test_return_str(self):
        origin = Origin.objects.get(id=1)
        expected_object_name = f"{origin.street} - {origin.city}"
        self.assertEqual(origin.__str__(), expected_object_name)

    def test_if_zip_code_is_valid(self):
        origin = Origin.objects.get(id=1)
        validation = Shipping.validate_zip_code(origin.zip_code)
        self.assertFalse(validation)

    def test_data_created(self):
        origin = Origin.objects.get(id=1)
        self.assertEqual(origin.street, "Rua José Leopoldo Lima")
        self.assertEqual(origin.number, "1064")
        self.assertEqual(origin.complement, "Casa")
        self.assertEqual(origin.neighborhood, "Santa Maria da Vitória")
        self.assertEqual(origin.city, "Santa Maria da Vitória")
        self.assertEqual(origin.reference, "Barbearia")
        self.assertEqual(origin.state, "BA")
        self.assertEqual(origin.zip_code, "47640000")


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
            zip_code="88333425",
        )

    def test_return_str(self):
        destination = Destination.objects.get(id=1)
        expected_object_name = f"{destination.street} - {destination.city}"
        self.assertEqual(destination.__str__(), expected_object_name)

    def test_if_zip_code_is_valid(self):
        destination = Destination.objects.get(id=1)
        validation = Shipping.validate_zip_code(destination.zip_code)
        self.assertFalse(validation)

    def test_data_created(self):
        destination = Destination.objects.get(id=1)
        self.assertEqual(destination.street, "Rua Sabino Pedro")
        self.assertEqual(destination.number, "16")
        self.assertEqual(destination.complement, "Restaurante")
        self.assertEqual(destination.neighborhood, "Laranjeiras")
        self.assertEqual(destination.city, "Balneário Camboriú")
        self.assertEqual(destination.reference, "Escola Edir")
        self.assertEqual(destination.state, "SC")
        self.assertEqual(destination.zip_code, "88333425")


class ShippingModelTestCase(TestCase):
    def test_return_str(self):
        origin = Origin.objects.create(
            street="Rua José Leopoldo Lima",
            number="1064",
            complement="Casa",
            neighborhood="Santa Maria da Vitória",
            city="Santa Maria da Vitória",
            reference="Barbearia",
            state="BA",
            zip_code="47640000",
        )
        destination = Destination.objects.create(
            street="Rua Sabino Pedro",
            number="16",
            complement="Restaurante",
            neighborhood="Laranjeiras",
            city="Balneário Camboriú",
            reference="Escola Edir",
            state="SC",
            zip_code="88333425",
        )
        Shipping.objects.create(origin=origin, destination=destination)

        shipping = Shipping.objects.get(id=1)
        expected_object_name = (
            f"Origin: {shipping.origin} | Destination: {shipping.destination}"
        )
        self.assertEqual(shipping.__str__(), expected_object_name)
