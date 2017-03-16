from __future__ import unicode_literals

from django.db import models

class Submission(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=155, null=False)
	app_type = models.BigIntegerField(default=0)
	app_url = models.CharField(max_length=255, blank=True, null=False)
	code_url = models.CharField(max_length=255, blank=False, null=False)
	thumbnail_url = models.CharField(max_length=255, blank=True, null=False)
	description = models.CharField(max_length=2000, null=False)
	first_name = models.CharField(max_length=255, null=False)
	last_name = models.CharField(max_length=255, null=False)
	email_address = models.CharField(max_length=255, null=False)
	member1 = models.CharField(max_length=255, blank=True, null=True)
	member2 = models.CharField(max_length=255, blank=True, null=True)
	member3 = models.CharField(max_length=255, blank=True, null=True)
	comments = models.CharField(max_length=2000, blank=True, null=True)
	last_update = models.DateTimeField()
	date_created = models.DateTimeField()

	class Meta:
		db_table = 'submission'

class SubmissionLikes(models.Model):
	id = models.AutoField(primary_key=True)
	submission = models.ForeignKey('Submission', models.DO_NOTHING)
	ip = models.CharField(max_length=255, blank=True, null=False)
	last_update = models.DateTimeField(blank=True, null=True)
	date_created = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = 'likes'