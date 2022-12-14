# Generated by Django 4.1 on 2022-09-06 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shipping", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shipping",
            name="destination",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shipping.destination",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="shipping",
            name="origin",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shipping.origin",
            ),
            preserve_default=False,
        ),
    ]
