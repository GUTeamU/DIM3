from django.db import models
from social_auth.backends import *
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User) # leave as blank=False to force at least one member

    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    description = models.TextField()
    project = models.ForeignKey(Project)
    category = models.TextField(max_length=16)

    def __unicode__(self):
        return self.title
