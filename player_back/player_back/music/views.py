from django.shortcuts import render
from rest_framework import viewsets
from player_back.music.serializers import *

from player_back.music.models import Album

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    permission_classes = []

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer
    permission_classes = []

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer
    permission_classes = []

class AlbumArtistsViewSet(viewsets.ModelViewSet):
    queryset = AlbumArtists.objects.all().order_by('id')
    serializer_class = AlbumArtistsSerializer
    permission_classes = []

class AlbumSongsViewSet(viewsets.ModelViewSet):
    queryset = AlbumSongs.objects.all().order_by('id')
    serializer_class = AlbumSongsSerializer
    permission_classes = []

