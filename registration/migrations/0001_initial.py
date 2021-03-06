# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('voter_id', models.IntegerField()),
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('party_id', models.IntegerField()),
                ('election_id', models.IntegerField()),
                ('college_id', models.CharField(max_length=9)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'candidate',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('registration_no', models.IntegerField()),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('year', models.DateField()),
            ],
            options={
                'db_table': 'election',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('party_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('registration_no', models.IntegerField()),
                ('symbol', models.FileField(upload_to='party-symbol')),
            ],
            options={
                'db_table': 'Party',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=30, unique=True)),
                ('post_election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Election')),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('voter_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('dob', models.DateField()),
                ('disability', models.CharField(max_length=50)),
                ('college_id', models.CharField(max_length=9)),
                ('citizenship_no', models.CharField(max_length=20)),
                ('photo', models.FileField(upload_to='student-photo')),
                ('is_verified', models.BooleanField(default=False)),
                ('college_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.College')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='WinnerReport',
            fields=[
                ('post', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('candidate_id', models.IntegerField()),
                ('votes', models.IntegerField()),
                ('election_id', models.IntegerField()),
            ],
            options={
                'db_table': 'winner_report',
            },
        ),
        migrations.AddField(
            model_name='candidate',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Post'),
        ),
    ]
