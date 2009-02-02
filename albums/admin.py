from django.contrib import admin
from musikbiblio.albums.models import Album, AlbumSongs
from musikbiblio.songs.models import Song

class AlbumSongsInline(admin.TabularInline):
  model = AlbumSongs
  extra = 1

class AlbumOptions(admin.ModelAdmin):
  inlines = [AlbumSongsInline]

admin.site.register(Album, AlbumOptions)
