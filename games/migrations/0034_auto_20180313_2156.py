# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-13 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0033_batterorder_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batterorder',
            name='batseat1',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='batseat2',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='batseat3',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='batseat4',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='batseat5',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='player',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='batterorder',
            name='team',
        ),
        migrations.DeleteModel(
            name='BatterOrder',
        ),
    ]
