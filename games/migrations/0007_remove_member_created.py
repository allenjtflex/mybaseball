# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_team_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='created',
        ),
    ]