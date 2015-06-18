from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ideas_from/', views.ideas_from,name='ideas_from'),
]