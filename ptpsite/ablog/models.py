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

class Post(models.Model):
	image = models.CharField(max_length=225)
	title = models.CharField(max_length=225)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category= models.CharField(max_length=225)
	body = RichTextField(blank=True, null=True)
	
	#body = models.TextField()
	desc = models.TextField(max_length=100)
	date_post = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('post-detail', args=(str(self.id)))

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=225)
	body = models.TextField()
	date_comment = models.DateField(auto_now_add=True)

	

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
	
