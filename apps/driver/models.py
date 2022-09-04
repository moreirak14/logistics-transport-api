import enum

from django.db import models

from apps.driver.exceptions import VehicleTypeInvalid


class VehicleTypes(enum.Enum):
    TRUCK_3_4 = "1"
    TRUCK_TOCO = "2"
    TRUCK_TRUCK = "3"
    TRUCK_SIMPLES = "4"
    TRUCK_EIXO = "5"


class Driver(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=50, null=False)
    own_vehicle = models.BooleanField(default=False)
    driver_license = models.CharField(max_length=5, null=False)
    loaded = models.BooleanField(default=False)
    vehicle_types = models.CharField(max_length=50, null=False)

    @staticmethod
    def validate_vehicle_types(vehicle_types: str):
        try:
            vehicle_types = VehicleTypes(vehicle_types).value
        except ValueError as e:
            raise VehicleTypeInvalid(
                f"Vehicle Types {vehicle_types} is invalid"
            ) from e

    def __str__(self):
        return self.first_name
