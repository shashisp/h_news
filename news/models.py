from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Article(models.Model):
	""" Model to  store all hacker news article attributes
	"""
	title = models.CharField(max_length=250, null=True)
	hn_id = models.IntegerField(blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	url = models.URLField()
	hn_url = models.URLField(blank=True)
	posted_on = models.DateTimeField()
	up_votes = models.IntegerField(blank=True, default=0)
	comments = models.IntegerField(blank=True, default=0)
	posted_by = models.ForeignKey(User, null=True)
	rank = models.IntegerField(blank=True, default=0)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('-posted_on',)

	def save(self, *args, **kwargs):
		""" while adding articles manually store slug as hacker news url
		"""
		if not self.hn_url:
			self.hn_url = slugify(self.title)
		super(Article, self).save(*args, **kwargs)



class Vote(models.Model):
	""" Model To track Votes
	"""
	article = models.ForeignKey(Article)
	voted_by = models.ForeignKey(User)

	def __unicode__(self):
		return "%s voted %s" % (self.voted_by.username, self.article.title)


class Read(models.Model):
	""" Model to track readlog
	"""
	article = models.ForeignKey(Article)
	read_by = models.ForeignKey(User)

	def __unicode__(self):
		return "%s read by %s" % (self.article.title, self.read_by.username)


class Delete(models.Model):
	""" Model to track delete logs
	"""
	article = models.ForeignKey(Article)
	deleted_by = models.ForeignKey(User)

	def __unicode__(self):
		return "%s deleted by %s" % (self.article.title, self.deleted_by.username)