# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11 on 2018-04-16 15:53
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
=======
# Generated by Django 1.11 on 2018-04-05 13:11
from __future__ import unicode_literals

from django.conf import settings
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(choices=[('R', 'raw'), ('C', 'composite')], max_length=1)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
<<<<<<< HEAD
=======
                ('url', models.CharField(blank=True, max_length=100)),
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab
            ],
        ),
        migrations.CreateModel(
            name='UserParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='metric',
            name='participation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.UserParticipation'),
        ),
=======
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab
    ]
