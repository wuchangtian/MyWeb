# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-23 03:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0018_auto_20171222_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='users.Tag')),
            ],
        ),
    ]
