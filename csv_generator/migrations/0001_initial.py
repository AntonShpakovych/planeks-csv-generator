# Generated by Django 4.2.6 on 2023-10-17 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Schema",
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
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "column_separator",
                    models.CharField(
                        choices=[
                            (",", "Comma"),
                            (" ", "Space"),
                            (";", "Semicolon"),
                            ("|", "Vertical line"),
                            ("/", "Slash"),
                        ],
                        default=",",
                        max_length=1,
                    ),
                ),
                (
                    "string_character",
                    models.CharField(
                        choices=[
                            ('"', "Double quotes"),
                            ("'", "Single quotes"),
                            ('"""', "Triple quotes"),
                        ],
                        default="'",
                        max_length=3,
                    ),
                ),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataSet",
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
                ("rows", models.IntegerField(default=1)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("processing", "Processing"),
                            ("ready", "Ready"),
                        ],
                        default="available",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="datasets",
                        to="csv_generator.schema",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Column",
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
                ("name", models.CharField(max_length=255)),
                ("order", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("full_name", "Full name"),
                            ("integer", "Integer"),
                            ("company", "Company"),
                            ("job", "Job"),
                            ("email", "Email"),
                        ],
                        max_length=9,
                    ),
                ),
                ("integer_from", models.IntegerField(blank=True, null=True)),
                ("integer_to", models.IntegerField(blank=True, null=True)),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="csv_generator.schema",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "schema"), ("schema", "order")},
            },
        ),
    ]