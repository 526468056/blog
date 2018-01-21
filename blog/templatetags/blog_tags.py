from django import template
from ..models import  Tag,Post,Category
from random import choice

register=template.Library()

@register.simple_tag
def get_tags():
	return Tag.objects.all()

@register.simple_tag
def get_tag(id):
	post=Post.objects.get(pk=id)
	return post.tags.all()

@register.simple_tag
def get_categorys():
	
	category=Category.objects.all()
	return category

@register.simple_tag
def get_color():
	color=['DodgerBlue','LimeGreen','Turquoise','CornflowerBlue ','SkyBlue','gray','peru','LightCoral','rgb(0, 133, 161)','rgb(140, 174, 219)','rgb(187, 187, 238)']
	return choice(color)



