from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

# Create your views here.

class LoginView(View):
    __template__ = 'auth_user/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)

    def post(self, request, *args, **kwargs):
        return redirect('home')

class RegisterView(View):
    __template__ = 'auth_user/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)

    def post(self, request, *args, **kwargs):
        return redirect('home')


@method_decorator(login_required(login_url='login'), name='dispatch')
class IndexView(View):
    __template__ = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)


@method_decorator(login_required(login_url='login'), name='dispatch')
class MusicView(View):
    __template__ = 'music/music.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)


@method_decorator(login_required(login_url='login'), name='dispatch')
class MusicUploadView(View):
    __template__ = 'music_upload/music_upload.html'

    def get(self, music_slug, request, *args, **kwargs):
        return render(request, template_name=self.__template__)


@method_decorator(login_required(login_url='login'), name='dispatch')
class PlaylistView(View):
    __template__ = 'playlist/playlist_view.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)


@method_decorator(login_required(login_url='login'), name='dispatch')
class PlaylistCreateView(View):
    __template__ = 'playlist_create/playlist_create.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.__template__)


@method_decorator(login_required(login_url='login'), name='dispatch')
class PlaylistUpdateView(View):
    __template__ = 'playlist_update/playlist_update.html'

    def get(self, playlist_slug, request, *args, **kwargs):
        return render(request, template_name=self.__template__)
