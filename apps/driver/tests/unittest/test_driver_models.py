from django.test import TestCase

from apps.driver.models import Driver


class DriverModelTestCase(TestCase):
    def setUp(self):
        Driver.objects.create(
            first_name="José",
            last_name="Sei lá",
            age=52,
            gender="M",
            own_vehicle=True,
            driver_license="D-E",
            loaded=False,
            vehicle_types="5",
        )

    def test_return_str(self):
        driver = Driver.objects.get(id=1)
        expected_object_name = f"{driver.first_name} {driver.last_name}"
        self.assertEqual(driver.__str__(), expected_object_name)

    def test_data_created(self):
        driver = Driver.objects.get(id=1)
        self.assertEqual(driver.first_name, "José")
        self.assertEqual(driver.last_name, "Sei lá")
        self.assertEqual(driver.age, 52)
        self.assertEqual(driver.gender, "M")
        self.assertTrue(driver.own_vehicle)
        self.assertEqual(driver.driver_license, "D-E")
        self.assertFalse(driver.loaded)
        self.assertEqual(driver.vehicle_types, "5")
