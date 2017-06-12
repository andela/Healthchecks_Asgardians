from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/create/$', views.create_post, name='create_post'),
    url(r'^post/(?P<pk>\d+)/view/$', views.post_view, name='post_view'),
    url(r'^blogpost/$', views.blog_list, name='blog_list'),
    url(r'^blog/$', views.view_blog, name='hc-blog'),
]
