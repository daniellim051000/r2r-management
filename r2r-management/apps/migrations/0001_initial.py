# Generated by Django 5.1.3 on 2024-11-13 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PropertyArea",
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
                ("area_name", models.CharField(max_length=255)),
                ("area_description", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Property Area",
                "verbose_name_plural": "Property Area",
                "db_table": "property_area",
            },
        ),
        migrations.CreateModel(
            name="BusinessUnit",
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
                ("unit_number", models.CharField(max_length=100)),
                ("unit_name", models.CharField(max_length=100)),
                ("unit_rental", models.IntegerField()),
                ("unit_address", models.CharField(max_length=255, null=True)),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps.propertyarea",
                    ),
                ),
            ],
            options={
                "verbose_name": "Business Unit",
                "verbose_name_plural": "Business Units",
                "db_table": "business_unit",
            },
        ),
        migrations.CreateModel(
            name="RoomDetails",
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
                ("room_name", models.CharField(max_length=100)),
                ("best_case_rental", models.IntegerField()),
                ("worst_case_rental", models.IntegerField()),
                ("actual_rental", models.IntegerField(null=True)),
                ("is_rental", models.BooleanField(default=False)),
                (
                    "business_unit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps.businessunit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Room Detail",
                "verbose_name_plural": "Room Details",
                "db_table": "room_details",
            },
        ),
        migrations.CreateModel(
            name="RoomPhoto",
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
                ("photo_name", models.CharField(max_length=255)),
                ("photo_path", models.ImageField(upload_to="")),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps.roomdetails",
                    ),
                ),
            ],
            options={
                "verbose_name": "Room Photo",
                "verbose_name_plural": "Room Photos",
                "db_table": "room_photos",
            },
        ),
        migrations.CreateModel(
            name="UnitFileAttachment",
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
                ("file_name", models.CharField(max_length=255)),
                ("file_path", models.FileField(upload_to="")),
                (
                    "business_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps.businessunit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Unit Attachment",
                "verbose_name_plural": "Unit Attachments",
                "db_table": "unit_attachment",
            },
        ),
    ]