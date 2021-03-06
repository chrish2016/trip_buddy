# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20180904_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='planner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reglogin.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travelers',
            field=models.ManyToManyField(related_name='trips', to='reglogin.User'),
        ),
    ]
