# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-24 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20171224_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/static/photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar2',
            field=models.ImageField(blank=True, null=True, upload_to='users/static/photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar3',
            field=models.ImageField(blank=True, null=True, upload_to='users/static/photo'),
        ),
        migrations.AlterField(
            model_name='works',
            name='work',
            field=models.ImageField(blank=True, null=True, upload_to='users/static/photo'),
        ),
    ]
