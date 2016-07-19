# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 23:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_articles_allowed_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='allowed_guilds',
            field=models.ManyToManyField(related_name='guilds_allowed', to='website.Guilds'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='allowed_users',
            field=models.ManyToManyField(related_name='articles_allowed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articles',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_written', to=settings.AUTH_USER_MODEL),
        ),
    ]
