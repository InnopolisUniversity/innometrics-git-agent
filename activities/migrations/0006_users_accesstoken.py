# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-13 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20180129_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='accesstoken',
            field=models.CharField(default='abc', max_length=30),
            preserve_default=False,
        ),
    ]