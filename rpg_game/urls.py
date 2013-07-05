from django.conf.urls import patterns, url

from rpg_game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/play_game/$', views.play_game, name='play_game'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/add_char/$', views.add_char, name ='add_char')
)
