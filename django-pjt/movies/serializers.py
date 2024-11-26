from .models import Movie, MoviePicks
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MoviePicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePicks
        fields = '__all__'