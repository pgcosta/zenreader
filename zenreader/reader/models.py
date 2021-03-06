from django.db import models

# Create your models here.

class Tweet(models.Model):
  name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  message = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  
  def __unicode__(self):
    return self.name + ':  ' + self.message
