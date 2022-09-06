# Generated by Django 4.1 on 2022-09-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shipping", "0002_alter_shipping_destination_alter_shipping_origin"),
        ("driver", "0002_driver_shipping"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="shipping",
            field=models.ManyToManyField(blank=True, null=True, to="shipping.shipping"),
        ),
    ]
