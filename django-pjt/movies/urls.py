from django.urls import path
from . import views

urlpatterns = [
    path('now-on/', views.nowon)
]
