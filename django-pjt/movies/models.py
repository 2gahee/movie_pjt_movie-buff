from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    director = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    vote_average = models.DecimalField(max_digits=4, decimal_places=3)
    poster_path = models.CharField(max_length=50)
    release_date = models.DateField()
    now_playing = models.BooleanField()
    popularity = models.FloatField()
    
class UserMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.CharField(max_length=50)

class Cinema(models.Model):
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=200)