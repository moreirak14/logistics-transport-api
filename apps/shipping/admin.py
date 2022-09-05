from django.contrib import admin

from apps.shipping.models import Destination, Origin, Shipping

admin.site.register(Shipping)
admin.site.register(Origin)
admin.site.register(Destination)
