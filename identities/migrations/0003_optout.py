# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identities', '0002_auto_20160204_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_source', models.CharField(max_length=100)),
                ('request_source_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identities.Identity')),
            ],
        ),
    ]
