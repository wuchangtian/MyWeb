# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-21 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_category_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
