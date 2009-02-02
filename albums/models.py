from django.db import models
from musikbiblio.artists.models import Artist
from musikbiblio.songs.models import Song

# Create your models here.
class Album(models.Model):
  name = models.CharField(max_length=150, primary_key=True)
  artist = models.ManyToManyField(Artist)
  songs = models.ManyToManyField(Song, through='AlbumSongs')
  year = models.DateField()
  tracks = models.IntegerField()
  discs = models.IntegerField()
  compilation = models.BooleanField()
  coverArt = models.FileField(upload_to='covers')

  def __unicode__(self):
    return "[%s] %s" % (self.year.strftime("%Y"), self.name)

class AlbumSongs(models.Model):
  album = models.ForeignKey(Album)
  song = models.ForeignKey(Song)
  track = models.IntegerField()
  disc = models.IntegerField()

