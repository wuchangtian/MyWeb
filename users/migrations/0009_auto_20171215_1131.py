# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-15 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171214_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar4',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar5',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar6',
        ),
    ]
