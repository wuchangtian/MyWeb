# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-04 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20180104_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]