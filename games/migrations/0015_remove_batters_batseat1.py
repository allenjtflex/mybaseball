# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20180307_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batters',
            name='batseat1',
        ),
    ]
