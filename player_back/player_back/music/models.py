from django.db import models

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 256)
	nacionality = models.CharField(max_length = 256)
	#top_songs = models.CharField(max_length = 256)
	def __str__(self):
		return f'{self.name}'

class Song(models.Model):
	name = models.CharField(max_length = 256)
	audio = models.TextField(null=True)
	song_length = models.SmallIntegerField()
	num_plays = models.IntegerField(default=0)
	def __str__(self):
		return f'{self.name}'

class Album(models.Model):
	name = models.CharField(max_length = 256)
	genre = models.CharField(max_length = 256)
	launch_date = models.DateField(null=True) 
	img = models.TextField(null=True)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	songs = models.ManyToManyField(Song, through='AlbumSongs')
	artists = models.ManyToManyField(Artist, through='AlbumArtists')
	def __str__(self):
		return f'{self.name}'


class AlbumArtists(models.Model):
	album = models.ForeignKey(Album, related_name='AlbumWithArtists', on_delete=models.DO_NOTHING)
	artist = models.ForeignKey(Artist, related_name='ArtistsWithAlbums', on_delete=models.DO_NOTHING)
	def __str__(self):
		return f'{self.id}'


class AlbumSongs(models.Model):
	album = models.ForeignKey(Album, related_name='AlbumWithSongs', on_delete=models.DO_NOTHING)
	song = models.ForeignKey(Song, related_name='ArtistsWithAlbums', on_delete=models.DO_NOTHING)
	def __str__(self):
		return f'{self.id}'
