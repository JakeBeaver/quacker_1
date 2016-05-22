from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
	body = models.TextField()
	time = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.body [0:20]


class authpost(models.Model):
	body = models.TextField()
	time = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User)
	def __unicode__(self):
		return self.owner.username + ": " + self.body [0:20]
	

class comment(models.Model):
	body = models.TextField()
	time = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User)
	post = models.IntegerField()
	def __unicode__(self):
		return str(self.post) + ", " + self.owner.username + ": " + self.body [0:20]
