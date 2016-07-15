# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 05:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_guilds_guild_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guilds',
            old_name='guild_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='guilds',
            old_name='guild_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='guilds',
            old_name='guild_leader',
            new_name='leader',
        ),
        migrations.RenameField(
            model_name='guilds',
            old_name='guild_name',
            new_name='name',
        ),
    ]
