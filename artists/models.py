from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=100, primary_key=True)

  def __unicode__(self):
    return self.name
