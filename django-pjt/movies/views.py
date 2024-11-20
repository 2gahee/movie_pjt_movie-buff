from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
import requests
from rest_framework.exceptions import NotFound
from django.conf import settings
# Create your views here.

@api_view(["GET"])
def movie_list(request):
    url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KOR&page=1&region=KR"

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
    url = "https://api.themoviedb.org/3/movie/popular?language=ko-KOR&region=KR"

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

