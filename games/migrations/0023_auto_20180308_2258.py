# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0022_remove_batterorder_batseat6'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_finished',
            field=models.BooleanField(default=True, verbose_name=''),
        ),
    ]