# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-04 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20180104_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='avatar',
            new_name='author',
        ),
    ]
