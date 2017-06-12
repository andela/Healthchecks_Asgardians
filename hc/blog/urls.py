from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^post/create/$', views.create_post, name='create_post'),
    url(r'^post/(?P<pk>\d+)/view/$', views.post_view, name='post_view'),
    url(r'^blogpost/$', views.blog_list, name='blog_list'),
    url(r'^blog/$', views.view_blog, name='blog')
=======
    url(r'^blog/create_post/$', views.create_post, name='create_post'),
    url(r'^post/(?P<pk>\d+)/view/$', views.post_view, name='post_view'),
    url(r'^blog/$', views.blogs, name="hc-blogs")
>>>>>>> f3653bbaf0e055518b179d7b7b0c754d04894488
]
