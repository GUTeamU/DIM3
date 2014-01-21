from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    description = models.TextField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name
