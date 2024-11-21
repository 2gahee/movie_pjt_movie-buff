from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import UserMovie
from .serializers import MovieSerializer
import requests
from rest_framework.exceptions import NotFound
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(["GET"])
def movie_list(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=ko-KOR&page=1&region=KR"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.TMDB_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise NotFound(detail="TMDB API 호출에 실패했습니다.")
    data = response.json()
    now_ons = data.get("results", [])
    print(now_ons)
    return Response(now_ons)

@api_view(["GET"])
def nowon(request):
    url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KOR&region=KR"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.TMDB_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise NotFound(detail="TMDB API 호출에 실패했습니다.")
    data = response.json()
    movies = data.get("results", [])  # 'results' 키에서 영화 데이터 추출
    print(movies)
    return Response(movies)

@api_view(["GET"])
def movieDetail(request, movieId):
    url = f'https://api.themoviedb.org/3/movie/{movieId}?language=ko-KOR'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.TMDB_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise NotFound(detail="TMDB API 호출에 실패했습니다.")
    data = response.json()
    print(data)
    return Response(data)

@login_required
@api_view(["OPTIONS", "POST"])
def movieLike(request, movieId):
    user = request.user
    try:
        user_movie = UserMovie.objects.filter(user=user, movie=movieId).first()
        if user_movie:
            user_movie.delete()
        else:
            UserMovie.objects.create(user=user, movie=movieId)
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    