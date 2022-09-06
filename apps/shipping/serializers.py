from rest_framework import serializers

from apps.shipping.models import Destination, Origin, Shipping


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

    def create(self, validated_data) -> Shipping:
        origin = Origin.objects.create(**validated_data["origin"])
        destination = Destination.objects.create(**validated_data["destination"])
        shipping = Shipping(origin=origin, destination=destination)
        shipping.save()
        return shipping
