# Generated by Django 4.1 on 2022-09-05 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destination",
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
                ("street", models.CharField(max_length=120)),
                ("number", models.CharField(max_length=60)),
                ("complement", models.CharField(max_length=120)),
                ("neighborhood", models.CharField(max_length=60)),
                ("city", models.CharField(max_length=60)),
                ("reference", models.CharField(max_length=60)),
                ("state", models.CharField(max_length=10)),
                ("zip_code", models.CharField(max_length=20)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Origin",
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
                ("street", models.CharField(max_length=120)),
                ("number", models.CharField(max_length=60)),
                ("complement", models.CharField(max_length=120)),
                ("neighborhood", models.CharField(max_length=60)),
                ("city", models.CharField(max_length=60)),
                ("reference", models.CharField(max_length=60)),
                ("state", models.CharField(max_length=10)),
                ("zip_code", models.CharField(max_length=20)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Shipping",
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
                (
                    "destination",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shipping.destination",
                    ),
                ),
                (
                    "origin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shipping.origin",
                    ),
                ),
            ],
        ),
    ]
