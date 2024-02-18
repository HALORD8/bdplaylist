# Generated by Django 5.0.2 on 2024-02-18 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_data', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('music_author', models.CharField(max_length=128)),
                ('music_name', models.CharField(max_length=128)),
                ('music_img', models.ImageField(upload_to='media/thumb_music/')),
                ('music_file', models.FileField(upload_to='media/musics/')),
                ('music_slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_data', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('playlist_name', models.CharField(max_length=128)),
                ('playlist_img', models.ImageField(upload_to='media/playlist/')),
                ('playlist_slug', models.SlugField()),
                ('playlist_musics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.music')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
