from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import UserMovie, MoviePicks
from .serializers import MoviePicksSerializer
import requests
from rest_framework.exceptions import NotFound
from django.conf import settings
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import json
# Create your views here.

@api_view(["GET"])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def movieSearch(request):
    url = 'https://api.themoviedb.org/3/search/movie'
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({"error": "검색어를 입력하세요."}, status=400)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.TMDB_API_KEY}"
    }
    response = requests.get(url, headers=headers, params={"query": query, "include_adult": "true", "language": "ko-KR"})
    if response.status_code != 200:
        raise NotFound(detail="TMDB API 호출에 실패했습니다.")
    data = response.json()
    movies = data.get("results", [])  # 'results' 키에서 영화 데이터 추출
    return Response(movies)
    # return Response(movies)
    # title_query = request.GET.get('title', '')
    # if title_query:
    #     articles = Article.objects.filter(title__icontains=title_query)
    # else:  # 검색 조건이 없으면 전체 리스트 반환
    #     articles = Article.objects.all()
    # serializer = ArticleListSerializer(articles, many=True)
    # return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
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

# @login_required
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
    
@api_view(["GET"])
def likeMovieList(request):
    user = request.user
    try:
        user_movie = UserMovie.objects.filter(user=user)
        liked_list = [um.movie for um in user_movie]
        movies_data = []
        for movie_id in liked_list:
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=ko-KOR'
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {settings.TMDB_API_KEY}"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                movie_data = response.json()
                movies_data.append({
                    "id": movie_data.get("id"),
                    "title": movie_data.get("title"),
                    "poster_path": movie_data.get("poster_path")
                })
            else:
                print(f"Failed to fetch movie data for movie_id {movie_id}")
        return Response({'liked_list': movies_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@permission_classes([AllowAny])
def moviepicks_list(request):
    if request.method == "GET":
        title_query = request.GET.get('title', '')
        username_query = request.GET.get('username', '')
        content_query = request.GET.get('content', '')
        if title_query:
            movies = MoviePicks.objects.filter(title__icontains=title_query)
        elif username_query:
            movies = MoviePicks.objects.filter(user__username__icontains=username_query)
        elif content_query:
            movies = MoviePicks.objects.filter(content__icontains=content_query)
        else:  # 검색 조건이 없으면 전체 리스트 반환
            movies = MoviePicks.objects.all()
        serializer = MoviePicksSerializer(movies, many=True)
        return Response(serializer.data)