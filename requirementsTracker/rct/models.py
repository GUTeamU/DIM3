from django.db import models
from social_auth.backends import *
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    description = models.TextField()
    project = models.ForeignKey(Project)
    priority = models.TextField(max_length=1)
    category = models.TextField(max_length=16)

    def __unicode__(self):
        return self.title
