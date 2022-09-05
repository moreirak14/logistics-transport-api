from rest_framework import serializers

from apps.shipping.models import Destination, Origin, Shipping
from src.services.geolocation import GeolocationAPI


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = [
            "id",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "reference",
            "state",
            "zip_code",
            "latitude",
            "longitude",
        ]


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = [
            "id",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "reference",
            "state",
            "zip_code",
            "latitude",
            "longitude",
        ]


class ShippingSerializer(serializers.ModelSerializer):
    origin = OriginSerializer()
    destination = DestinationSerializer()

    class Meta:
        model = Shipping
        fields = "__all__"

    def get_geolocation(self, zip_code: str) -> None:
        service = GeolocationAPI()
        return service.geolocation(zip_code=zip_code)

    def create(self, validated_data) -> Shipping:
        origin = validated_data["origin"]
        del validated_data["origin"]
        destination = validated_data["destination"]
        del validated_data["destination"]

        shipping = Shipping.objects.create(**validated_data)

        if (origin, destination) is not None:
            if zip_code := origin["zip_code"]:
                if not Shipping.validate_zip_code(zip_code=zip_code):
                    coordinates = self.get_geolocation(zip_code=zip_code)
                    origin.latitude = coordinates["lat"]
                    origin.longitude = coordinates["lon"]
                    shipping_origin = Origin.objects.create(**origin)
                    shipping.origin = shipping_origin

            if zip_code := destination["zip_code"]:
                if not Shipping.validate_zip_code(zip_code=zip_code):
                    coordinates = self.get_geolocation(zip_code=zip_code)
                    destination.latitude = coordinates["lat"]
                    destination.longitude = coordinates["lon"]
                    shipping_destination = Destination.objects.create(
                        **destination)
                    shipping.destination = shipping_destination

        shipping.save()

        return shipping
