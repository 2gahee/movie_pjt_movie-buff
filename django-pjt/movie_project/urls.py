"""
URL configuration for movie_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import Profile
from accounts.views import ProfileUpdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/profile/', Profile.as_view(), name='profile'),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('community/', include('community.urls')),
    path('movies/', include('movies.urls')),
    path('events/', include('events.urls')),
    path('accounts/profile/update/', ProfileUpdate.as_view(), name='profile-update'),
]
