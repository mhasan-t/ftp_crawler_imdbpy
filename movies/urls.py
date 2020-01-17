from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.MovieList.as_view(), name='list'),
    path('<int:pk>/', views.MovieDetails.as_view(), name='details'),
    path('create/', views.MovieCreate.as_view(), name='create'),
    path('create-file/', views.addMovieWithFile.as_view(), name='create-file'),
    path('auto-create/', views.MovieAutoCreate.as_view(), name='auto-create')
]



