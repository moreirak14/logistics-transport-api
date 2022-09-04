from rest_framework.viewsets import ModelViewSet

from apps.driver.models import Driver
from apps.driver.serializers import DriverSerializer


class DriverView(ModelViewSet):
    serializer_class = DriverSerializer

    def get_queryset(self):
        return Driver.objects.all()
