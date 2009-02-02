from django.db import models
from musikbiblio.artists.models import Artist
from musikbiblio.genres.models import Genre

# Create your models here.
class Lyric(models.Model):
  text = models.TextField()
  composer = models.CharField(max_length=100)

class Song(models.Model):
  name = models.CharField(max_length=150,primary_key=True)
  artist = models.ManyToManyField(Artist)
  lyric = models.ForeignKey(Lyric)
  composer = models.CharField(max_length=100)
  genre = models.ForeignKey(Genre)
  comments = models.TextField()
