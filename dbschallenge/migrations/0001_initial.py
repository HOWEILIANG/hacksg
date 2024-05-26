# Generated by Django 4.2.13 on 2024-05-25 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InsuranceProduct",
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
                ("description", models.TextField()),
                ("premium", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                    "age",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(18),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                (
                    "comfortable_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                (
                    "bank_statement",
                    models.FileField(
                        blank=True, null=True, upload_to="bank_statements/"
                    ),
                ),
                (
                    "expected_returns",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        validators=[django.core.validators.MinValueValidator(1.0)],
                    ),
                ),
                (
                    "risk_appetite",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                        ],
                        default="Medium",
                        max_length=6,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Investment",
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
                ("amount_sgd", models.DecimalField(decimal_places=2, max_digits=15)),
                ("covered_with_insurance", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="investments",
                        to="dbschallenge.userprofile",
                    ),
                ),
            ],
        ),
    ]
