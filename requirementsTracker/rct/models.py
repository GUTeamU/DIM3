from django.db import models
from social_auth.backends import *
from django.contrib.auth.models import User



class UserProfile(models.Model):
	user = models.OneToOneField(User)

	

	def __unicode__(self):
		return self.user.username



# class CustomUserManager(models.Manager):
#     def create_user(self, username, email):
#         return self.model._default_manager.create(username=username)


# class CustomUser(models.Model):
#     username = models.CharField(max_length=128)
#     firstname = models.CharField(max_length=128)
#     lastname = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     email = models.CharField(max_length=128)
#     objects = CustomUserManager()


#     def is_authenticated(self):
#         return True

#     def social_extra_values(sender, user, response, details, **kwargs):
#     	result = False
#     	if "id" in response:

#     		from apps.photo.models import Photo
#     		from urllib2 import urlopen, HTTPError
#     		from django.template.defaultfilters import slugify
#     		from apps.account.utils import user_display
#     		from django.core.files.base import ContentFile

#     		try:
#     			url = None
#     			if sender == FacebookBackend:
#     				url = "http://graph.facebook.com/%s/picture?type=large" \
#     				% response["id"]
#     			elif sender == google.GoogleOAuth2Backend and "picture" in response:
#     				url = response["picture"]
#     			elif sender == TwitterBackend:
#     				url = response["profile_image_url"]

#     			if url:
#     				avatar = urlopen(url)
#     				photo = Photo(author = user, is_avatar = True)
#     				photo.picture.save(slugify(user.username + " social") + '.jpg',ContentFile(avatar.read()))

#     				photo.save()

#     		except HTTPError:
#     				pass
#     		result = True

#     	return result


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    description = models.TextField()
    project = models.ForeignKey(Project)
    priority = models.TextField()
    category = models.TextField()

    def __unicode__(self):
        return self.title
