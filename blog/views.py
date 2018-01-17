from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Post,Tag
import markdown
from django.shortcuts import get_object_or_404 
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
class IndexView(generic.ListView):
	model=Post
	template_name='blog/index.html'
	context_object_name='Post'
	paginate_by = 10

class PostDetailView(generic.DetailView):
	model=Post
	template_name='blog/post.html'
	context_object_name='post'

	def get_object(self, queryset=None):
		# 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
		post = super(PostDetailView,self).get_object(queryset=None)
	
		post.body = markdown.markdown(post.body,extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			'markdown.extensions.toc',])

		return post
class TagView(generic.ListView):
	model=Post
	template_name='blog/index.html'
	context_object_name='Post'

	def get_queryset(self):
		tag=get_object_or_404(Tag,pk=self.kwargs.get('pk'))



		return tag.post_set.all()


def about(request):
	tem=loader.get_template('blog/about.html')
	return HttpResponse(tem.render())

def contact(request):
	
	return render(request,'blog/contact.html')

def sendemail(request):
	subject=request.POST['subject']
	message=request.POST['message']
	if subject and message:

		
		send_mail(subject='我的博客',message='from:'+subject+'\n'+message,from_email='18711045036@163.com',recipient_list=['526468056@qq.com'])
		return HttpResponseRedirect(reverse('blog:index'))
		
		
	else:
		print(request.POST)
		return render(request,'blog/contact.html',{'error_message':"请填写完整！！！"})
		

		

