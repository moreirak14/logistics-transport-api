from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.driver.models import Driver
from apps.driver.serializers import DriverSerializer


class DriverView(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = DriverSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if vehicle_types := data["vehicle_types"]:
            Driver.validate_vehicle_types(vehicle_types=vehicle_types)

        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        own_vehicle = self.request.query_params.get("own_vehicle", None)
        loaded = self.request.query_params.get("loaded", None)

        if own_vehicle is not None:
            return Driver.objects.filter(own_vehicle=own_vehicle)

        if loaded is not None:
            return Driver.objects.filter(loaded=loaded)

        return Driver.objects.all()
