# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0019_auto_20180308_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='batterorder',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
            preserve_default=False,
        ),
    ]
