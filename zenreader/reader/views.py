# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from reader.models import Tweet

def index(request):
  tweetList = Tweet.objects.order_by('-pub_date')[:5]
  template = loader.get_template('reader/index.html')
  context = RequestContext(request, {
        'tweetList': tweetList,
    })

  return HttpResponse(template.render(context))

def detailTweet(request, tweet_id):
    return HttpResponse("You're looking at tweet %s." % tweet_id)
