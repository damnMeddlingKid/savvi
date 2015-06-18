from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ideas_from/(?P<idea_id>[0-9]+)/(?P<page_limit>[0-9]+)/$', views.ideas_from,name='ideas_from'),
]