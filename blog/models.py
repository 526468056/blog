# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

import sys  
  
default_encoding = 'utf-8'  
if sys.getdefaultencoding() != default_encoding:  
    reload(sys)  
    sys.setdefaultencoding(default_encoding)



class Tag(models.Model):
	'''
	标签
	'''
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Category(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
			return self.name		

class Post(models.Model):
	'''
	文章
	'''
	#标题


    

	title=models.CharField(max_length=70)
	#创建时间和修改时间
	create_time=models.DateTimeField(default = timezone.now)
	modified_time=models.DateTimeField(auto_now = True)
	#正文
	body=models.TextField()
	#摘要
	excerpt=models.CharField(max_length=200,blank=True)
	#作者
	author=models.ForeignKey(User)
	#分类和标签
	
	
	tags=models.ManyToManyField(Tag,blank=True)
	category=models.ForeignKey(Category)
	imag=models.ImageField(upload_to='blog')
	views = models.PositiveIntegerField(default=0)

	def set_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def __str__(self):
		return self.title

	class Meta: 
		ordering = ['-create_time']










