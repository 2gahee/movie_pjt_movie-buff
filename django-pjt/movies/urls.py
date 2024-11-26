from django.urls import path
from . import views

urlpatterns = [
    path('now-on/', views.nowon),
    path('<int:movieId>/', views.movieDetail),
    path('<int:movieId>/like/', views.movieLike),
    path('liked_movies/', views.likeMovieList),
    path('moviepicks/', views.moviepicks_list),
    path('search/', views.movieSearch)
]
