# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170806_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.FileField(null=True, upload_to='static/candidates/'),
        ),
    ]