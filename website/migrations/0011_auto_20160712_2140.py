# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20160712_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guilds',
            name='guild_name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
