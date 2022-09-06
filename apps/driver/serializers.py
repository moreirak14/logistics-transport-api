from rest_framework import serializers

from apps.driver.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "gender",
            "own_vehicle",
            "driver_license",
            "loaded",
            "vehicle_types",
            "shipping",
        ]
