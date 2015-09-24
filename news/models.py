from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=250, null=True)
	hn_id = models.IntegerField()
	description = models.TextField(null=True, blank=True)
	url = models.URLField()
	hn_url = models.URLField()
	posted_on = models.CharField(max_length=150, null=True)
	up_votes = models.IntegerField()
	comments = models.IntegerField()
	posted_by = models.ForeignKey(User, null=True)

	def __unicode__(self):
		return self.title


class Log(models.Model):
	article = models.ForeignKey(Article)
	user = models.ForeignKey(User)
	is_read = models.NullBooleanField(default=False)
	is_deleted  = models.NullBooleanField(default=False)

	def __unicode__(self):
		return u"%s" % self.user


class Vote(models.Model):
	article = models.ForeignKey(Article)
	voted_by = models.ForeignKey(User)

	def __unicode__(self):
		return "%s voted %s" % (self.voted_by.username, self.article.title)