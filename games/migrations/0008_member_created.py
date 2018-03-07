# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_member_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]