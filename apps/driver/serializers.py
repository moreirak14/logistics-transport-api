from rest_framework import serializers

from apps.driver.models import Driver
from apps.shipping.serializers import ShippingSerializer


class DriverSerializer(serializers.ModelSerializer):
    shipping = ShippingSerializer(many=True)

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

    def _created_shipping(self, shipping, driver):
        serializer = ShippingSerializer()
        for data in shipping:
            shipping_full = serializer.create(validated_data=data)
            driver.shipping.add(shipping_full)

    def create(self, validated_data) -> Driver:
        shipping = validated_data["shipping"]
        del validated_data["shipping"]

        if vehicle_types := validated_data["vehicle_types"]:
            Driver.validate_vehicle_types(vehicle_types=vehicle_types)

        driver = Driver.objects.create(**validated_data)
        self._created_shipping(shipping=shipping, driver=driver)

        return driver
