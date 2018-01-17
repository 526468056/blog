from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
	'''
	标签
	'''
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

	def __str__(self):
		return self.title



