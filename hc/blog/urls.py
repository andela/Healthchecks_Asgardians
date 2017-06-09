from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/create/$', views.create_post, name='create_post')
]
