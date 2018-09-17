from django.conf.urls import url
from . import views


app_name = 'mysite'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^latest\.html$', views.IndexView.as_view(), name='latest'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='result'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote')
]