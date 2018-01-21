from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag_post'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category_post'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^sendemail/$',views.sendemail,name='sendemail'),
    

]
