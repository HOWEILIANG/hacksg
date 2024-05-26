# Generated by Django 4.2.13 on 2024-05-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbschallenge", "0003_treasuryyield"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reit",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("distribution_yield", models.FloatField()),
                ("price_to_book", models.FloatField()),
                ("dpu", models.FloatField()),
                ("nav", models.FloatField()),
                ("property_yield", models.FloatField()),
                ("gearing_ratio", models.FloatField()),
            ],
        ),
    ]