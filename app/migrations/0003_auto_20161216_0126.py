# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 01:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20161216_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='password',
        ),
        migrations.RemoveField(
            model_name='players',
            name='username',
        ),
        migrations.AddField(
            model_name='players',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
