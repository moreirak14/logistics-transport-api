from rest_framework import serializers
from apps.driver.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

    def create(self, validated_data):
        if vehicle_types := validated_data["vehicle_types"]:
            Driver.validate_vehicle_types(vehicle_types=vehicle_types)
        driver = Driver.objects.create(**validated_data)
        return driver
