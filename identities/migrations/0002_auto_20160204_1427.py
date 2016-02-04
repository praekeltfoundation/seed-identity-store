# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='communicate_through',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identities_communicate_through', to='identities.Identity'),
        ),
        migrations.AddField(
            model_name='identity',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identities_created_by', to='identities.Identity'),
        ),
    ]
