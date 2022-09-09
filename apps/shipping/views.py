from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.shipping.models import Shipping
from apps.shipping.serializers import ShippingSerializer


class ShippingView(ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

    def create(self, request: Request, *args, **kwargs):
        """
        :param request Creating shipping
        :return response Returns shipping data
        """
        data = request.data
        serializer = ShippingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
