from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<tweet_id>\d+)/$',views.detailTweet, name='Tweet')
  #url(r'^tweet/$',views.detailTweet)
)
