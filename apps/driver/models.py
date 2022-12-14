import enum

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.driver.exceptions import VehicleTypeInvalid
from apps.shipping.models import Shipping


class VehicleTypes(enum.Enum):
    TRUCK_3_4 = "1"
    TRUCK_TOCO = "2"
    TRUCK_TRUCK = "3"
    TRUCK_SIMPLES = "4"
    TRUCK_EIXO = "5"


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    own_vehicle = models.BooleanField(default=False)
    driver_license = models.CharField(max_length=5)
    loaded = models.BooleanField(default=False)
    vehicle_types = models.CharField(max_length=50)
    shipping = models.ForeignKey(
        Shipping, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def validate_vehicle_types(vehicle_types: str) -> None:
        """
        :argument vehicle_types
        :raise Validation vehicle types
        """
        try:
            vehicle_types = VehicleTypes(vehicle_types).value
        except ValueError as e:
            raise VehicleTypeInvalid(f"Vehicle Types {vehicle_types} is invalid") from e


@receiver(pre_save, sender=Driver)
def my_handler(sender, instance, **kwargs):
    if vehicle_types := instance.vehicle_types:
        Driver.validate_vehicle_types(vehicle_types=vehicle_types)
    return
