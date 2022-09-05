from django.db import models

from apps.shipping.exceptions import ZipCodeInvalid


class Origin(models.Model):
    street = models.CharField(max_length=120, null=False)
    number = models.CharField(max_length=60, null=False)
    complement = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    reference = models.CharField(max_length=60)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20, null=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.street} - {self.city}"


class Destination(models.Model):
    street = models.CharField(max_length=120, null=False)
    number = models.CharField(max_length=60, null=False)
    complement = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    reference = models.CharField(max_length=60)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20, null=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.street} - {self.city}"


class Shipping(models.Model):
    origin = models.ForeignKey(
        Origin, on_delete=models.CASCADE, null=True, blank=True)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Origin: {self.origin} | Destination: {self.destination}"
