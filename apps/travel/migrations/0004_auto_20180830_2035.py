# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reglogin', '0001_initial'),
        ('travel', '0003_auto_20180830_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.AddField(
            model_name='trip',
            name='travelers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='reglogin.User'),
        ),
    ]
