# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("identities", "0002_auto_20160204_1427"),
    ]

    operations = [
        migrations.CreateModel(
            name="OptOut",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="UUID of this optout request.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "optout_type",
                    models.CharField(
                        choices=[
                            ("stop", "No communication on address"),
                            ("stopall", "No communication on all addresses"),
                            ("unsubscribe", "Unsubcribe"),
                            ("forget", "Forget"),
                        ],
                        default="stop",
                        help_text="Type of optout request.",
                        max_length=20,
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        default="",
                        help_text="Address type used to identify the identity.",
                        max_length=50,
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        default="",
                        help_text="Address used to identify the identity.",
                        max_length=255,
                    ),
                ),
                (
                    "request_source",
                    models.CharField(
                        help_text="Service that the optout was requested from.",
                        max_length=100,
                    ),
                ),
                (
                    "requestor_source_id",
                    models.CharField(
                        help_text="ID for the user requesting the optout on the service that it was requested from. Ideally a UUID.",
                        max_length=500,
                        null=True,
                    ),
                ),
                (
                    "reason",
                    models.CharField(
                        help_text="Optional reason (e.g. 'not interested')",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Time request was received."
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="User creating the OptOut",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="optout_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        help_text="UUID for the identity opting out.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="identities.Identity",
                    ),
                ),
            ],
        )
    ]
