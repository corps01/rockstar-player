from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'artist',views.ArtistViewSet)
router.register(r'songs',views.SongViewSet)
router.register(r'album',views.AlbumViewSet)
router.register(r'albumartist', views.AlbumArtistsViewSet)
router.register(r'albumsongs', views.AlbumSongsViewSet)

urlpatterns = [
	path('', include(router.urls)),
]