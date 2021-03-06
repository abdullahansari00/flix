# Generated by Django 3.2.3 on 2021-05-31 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField(default=False, null=True)),
                ('movie_id', models.IntegerField(null=True)),
                ('language', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('genres', models.ManyToManyField(blank=True, to='geek.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='WatchedMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('movies', models.ManyToManyField(blank=True, to='geek.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
