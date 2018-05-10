# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-13 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0035_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatterOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('1', 'P'), ('2', 'C'), ('3', '1B'), ('4', '2B'), ('5', '3B'), ('6', 'SS'), ('7', 'LF'), ('8', 'CF'), ('9', 'RF'), ('DH', 'DH')], max_length=2)),
                ('batseat1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batseat1', to='games.BatResult')),
                ('batseat2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batseat2', to='games.BatResult')),
                ('batseat3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batseat3', to='games.BatResult')),
                ('batseat4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batseat4', to='games.BatResult')),
                ('batseat5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batseat5', to='games.BatResult')),
                ('gameschedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Schedule')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Team')),
            ],
        ),
    ]
