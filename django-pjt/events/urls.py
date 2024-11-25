from django.urls import path
from . import views

urlpatterns = [
    path('megabox/', views.megaboxEvents),
]
