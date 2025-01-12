# Generated by Django 5.1.4 on 2024-12-28 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("caption", models.TextField(max_length=2000)),
                ("media_url", models.URLField(max_length=500)),
                (
                    "media_type",
                    models.CharField(
                        choices=[("IMAGE", "Image"), ("VIDEO", "Video")],
                        default="IMAGE",
                        max_length=5,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("TECH", "Technology"),
                            ("ENT", "Entertainment"),
                            ("BUS", "Business"),
                            ("LIFE", "Lifestyle"),
                            ("FOOD", "Food"),
                            ("TRAV", "Travel"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("likes_count", models.PositiveIntegerField(default=0)),
                ("comments_count", models.PositiveIntegerField(default=0)),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
