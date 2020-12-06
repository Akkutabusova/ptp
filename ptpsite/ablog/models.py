from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name 
	
	def get_absolute_url(self):
		return reverse('home')
"""
class Tag_map(models.Model):

	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name 
	
	def get_absolute_url(self):
		return reverse('home')

class Category(models.Model):
	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name 
	
	def get_absolute_url(self):
		return reverse('home')

"""
class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to ="images/profile")
	website_url = models.CharField(max_length=225, null=True, blank=True )
	facebook_ur = models.CharField(max_length=225, null=True, blank=True )
	twitter_url = models.CharField(max_length=225, null=True, blank=True )
	linkedin_url = models.CharField(max_length=225, null=True, blank=True )
	github_url = models.CharField(max_length=225, null=True, blank=True )
	
	def __str__(self):
		return str(self.user)

	"""def __init__(self, arg):
		super Profile, self).__init__()
		self.arg = arg"""
	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to ="images/")
	title = models.CharField(max_length=225)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category= models.CharField(max_length=225)
	body = RichTextField(blank=True, null=True)
	
	#body = models.TextField()
	desc = models.TextField(max_length=100)
	date_post = models.DateField(auto_now_add=True)
	likes =models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()
		pass
	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('post-detail', args=(str(self.id)))
		return reverse('home')

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=225)
	body = models.TextField()
	date_comment = models.DateField(auto_now_add=True)

	

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
	
