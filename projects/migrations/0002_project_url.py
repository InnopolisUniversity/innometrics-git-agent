# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]