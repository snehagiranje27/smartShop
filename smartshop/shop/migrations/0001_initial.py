# Generated by Django 4.2.6 on 2023-10-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("items", models.CharField(max_length=1000)),
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=1000)),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("zipcode", models.CharField(max_length=200)),
                ("total", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("title", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("category", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.CharField(max_length=300)),
            ],
        ),
    ]
