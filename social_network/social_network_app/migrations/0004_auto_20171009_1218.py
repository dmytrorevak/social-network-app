# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_app', '0003_auto_20171009_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]