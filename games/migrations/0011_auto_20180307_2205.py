# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_cupgroup'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cupgroup',
            unique_together=set([('cup', 'team', 'group')]),
        ),
    ]
