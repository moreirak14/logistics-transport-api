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

    def create(self, validated_data) -> Driver:
        if vehicle_types := validated_data["vehicle_types"]:
            Driver.validate_vehicle_types(vehicle_types=vehicle_types)
        return Driver.objects.create(**validated_data)
