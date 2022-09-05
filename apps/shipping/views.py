from rest_framework.viewsets import ModelViewSet

from apps.shipping.models import Shipping
from apps.shipping.serializers import ShippingSerializer


class ShippingView(ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
