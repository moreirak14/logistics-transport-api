from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.shipping.exceptions import ZipCodeInvalid
from apps.shipping.services.geolocation import GeolocationAPI


class Origin(models.Model):
    street = models.CharField(max_length=120)
    number = models.CharField(max_length=60)
    complement = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    reference = models.CharField(max_length=60)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.street} - {self.city}"


class Destination(models.Model):
    street = models.CharField(max_length=120)
    number = models.CharField(max_length=60)
    complement = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    reference = models.CharField(max_length=60)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.street} - {self.city}"


class Shipping(models.Model):
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"Origin: {self.origin} | Destination: {self.destination}"

    @staticmethod
    def validate_zip_code(zip_code: str) -> None:
        """
        :argument zip_code
        :raise Validation zip code
        """
        if len(zip_code) != 8:
            raise ZipCodeInvalid(f"ZipCode {zip_code} is invalid")


@receiver(pre_save, sender=Shipping)
def shipping_pre_save(sender, instance, **kwargs):
    """
    :argument instance
    :return Save latitude and longitude of origin and destination
    """
    service = GeolocationAPI()

    def _save_lat_long(model):
        if zip_code := model.zip_code:
            Shipping.validate_zip_code(zip_code=zip_code)
            coordinates = service.get_geolocation(zip_code=zip_code)
            model.longitude = coordinates["lon"]
            model.latitude = coordinates["lat"]
            model.save()

    _save_lat_long(model=instance.origin)
    _save_lat_long(model=instance.destination)

    return instance
