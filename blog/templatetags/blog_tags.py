from django import template
from ..models import  Tag,Post

register=template.Library()

@register.simple_tag
def get_tags():
	return Tag.objects.all()

@register.simple_tag
def get_tag(id):
	post=Post.objects.get(pk=id)
	return post.tags.all()


