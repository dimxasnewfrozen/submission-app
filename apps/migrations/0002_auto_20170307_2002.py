# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-07 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(blank=True, max_length=255)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.RenameModel(
            old_name='Submissions',
            new_name='Submission',
        ),
        migrations.AlterModelTable(
            name='submission',
            table='submission',
        ),
        migrations.AddField(
            model_name='submissionlikes',
            name='submission_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apps.Submission'),
        ),
    ]