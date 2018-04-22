from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arts/all/$', views.arts, name='arts'),
    url(r'^art/(?P<art_id>\d+)/$', views.art, name='art'),
    url(r'^art/addlike/(?P<art_id>\d+)/$', views.addlike, name='addlike'),
    url(r'^art/addcomment/(?P<art_id>\d+)/$', views.addcomment, name='addcomment'),
    url(r'^addart/$', views.addart, name='addart'),
    url(r'^addartpost/$', views.addartpost, name='addartpost'),
    url(r'^folderadd/$', views.folderadd, name='folderadd'),
    url(r'^addfolderpost/$', views.addfolderpost, name='addfolderpost'),
    url(r'^userfolders/$', views.userfolders, name='userfolders'),
    url(r'^addartinfolder/(?P<art_id>\d+)/$', views.addartinfolder, name='addartinfolder'),
    url(r'^addfolderwithart/(?P<art_id>\d+)/$', views.addfolderwithart, name='addfolderwithart'),
    url(r'^addartinoldfolder/(?P<art_id>\d+)/$', views.addartinoldfolder, name='addartinoldfolder'),
    url(r'^artsfromfolder/(?P<folder_id>\d+)/$', views.artsfromfolder, name='artsfromfolder'),
]
