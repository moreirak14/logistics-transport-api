# Generated by Django 4.1 on 2022-09-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=50)),
                ("own_vehicle", models.BooleanField(default=False)),
                ("driver_license", models.CharField(max_length=5)),
                ("loaded", models.BooleanField(default=False)),
                ("vehicle_types", models.CharField(max_length=50)),
            ],
        ),
    ]
