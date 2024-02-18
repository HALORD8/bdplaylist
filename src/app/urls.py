from django.urls import path
from .views import (
    IndexView,
    MusicView,
    MusicUploadView,
    PlaylistView,
    PlaylistCreateView,
    PlaylistUpdateView,
    LoginView,
    RegisterView
)


urlpatterns = [
    # - Music -
    path('music/<slug:music_slug>/', MusicView.as_view(), name='music-view'),
    path('music-upload/', MusicUploadView.as_view(), name='music-upload'),

    # - Playlist -
    path('playlist/', PlaylistView.as_view(), name='playlist-view'),
    path('playlist/create/', PlaylistCreateView.as_view(), name='playlist-create'),
    path('playlist/update/<slug:playlist_slug>/', PlaylistUpdateView.as_view(), name='playlist-update'),

    # - Auth -
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    # - Home -
    path('', IndexView.as_view(), name='home')
]
