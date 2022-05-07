# Generated by Django 4.0.3 on 2022-05-06 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('launch_date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('nacionality', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('song_length', models.SmallIntegerField()),
                ('num_plays', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='AlbumWithSongs', to='music.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ArtistsWithAlbums', to='music.song')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumArtists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='AlbumWithArtists', to='music.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ArtistsWithAlbums', to='music.artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(through='music.AlbumArtists', to='music.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(through='music.AlbumSongs', to='music.song'),
        ),
    ]
