from rest_framework.viewsets import ModelViewSet

from apps.driver.models import Driver
from apps.driver.serializers import DriverSerializer


class DriverView(ModelViewSet):
    serializer_class = DriverSerializer

    def get_queryset(self):
        own_vehicle = self.request.query_params.get("own_vehicle", None)
        loaded = self.request.query_params.get("loaded", None)

        if own_vehicle is not None:
            return Driver.objects.filter(own_vehicle=own_vehicle)

        if loaded is not None:
            return Driver.objects.filter(loaded=loaded)

        return Driver.objects.all()
