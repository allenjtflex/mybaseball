# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0024_auto_20180308_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Schedule'),
        ),
    ]