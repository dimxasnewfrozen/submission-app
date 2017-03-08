# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=155)),
                ('app_url', models.CharField(blank=True, max_length=255)),
                ('code_url', models.CharField(blank=True, max_length=255)),
                ('thumbnail_url', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email_address', models.CharField(blank=True, max_length=255)),
                ('member1', models.CharField(blank=True, max_length=255, null=True)),
                ('member2', models.CharField(blank=True, max_length=255, null=True)),
                ('member3', models.CharField(blank=True, max_length=255, null=True)),
                ('member4', models.CharField(blank=True, max_length=255, null=True)),
                ('member5', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'submissions',
            },
        ),
    ]
