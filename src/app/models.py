from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class BaseAbstract(models.Model):
    upload_data = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Music(BaseAbstract):
    music_author = models.CharField(max_length=128, blank=False, null=False)
    music_name = models.CharField(max_length=128, blank=False, null=False)
    music_img = models.ImageField(upload_to='media/thumb_music/', blank=False, null=False)
    music_file = models.FileField(upload_to='media/musics/', blank=False, null=False)
    music_slug = models.SlugField(blank=False, null=False)

    def sav(self, *args, **kwargs):
        self.music_slug = slugify(self.music_name)
        super(Music, self).save(*args, **kwargs)

    def __str__(self):
        return self.music_name

class Playlist(BaseAbstract):
    playlist_name = models.CharField(max_length=128, blank=False, null=False)
    playlist_author = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_img = models.ImageField(upload_to='media/playlist/', blank=False, null=False)
    playlist_musics = models.ForeignKey(Music, on_delete=models.CASCADE)
    playlist_slug = models.SlugField(blank=False, null=False)

    def save(self, *args, **kwargs):
        self.playlist_slug = slugify(self.playlist_name)
        super(Playlist, self).save(*args, **kwargs)

    def __str__(self):
        return self.playlist_name