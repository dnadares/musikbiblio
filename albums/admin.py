from django.contrib import admin
from musikbiblio.albums.models import Album, AlbumSongs
from musikbiblio.songs.models import Song
from django.contrib import admin

admin.site.register(Album)

class AlbumSongsInline(admin.TabularInline):
  model = AlbumSongs

admin_content = admin.AdminSite()
admin_content.register(Song)
