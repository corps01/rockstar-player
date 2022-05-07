from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'nacionality']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'song_length', 'num_plays']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'genre', 'launch_date', 'img', 'price', 'songs', 'artists']
        depth = 1

class AlbumArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArtists
        fields = ['id', 'artist', 'album']

class AlbumSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumSongs
        fields = ['id', 'album', 'song']