# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170808_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postName', to='registration.Post'),
        ),
    ]
