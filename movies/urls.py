from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.MovieList.as_view(), name='list'),
    path('<int:pk>/', views.MovieDetails.as_view(), name='details'),
    path('watch/<int:pk>/', views.MovieWatch.as_view(), name='watch'),
    path('create/', views.MovieCreate.as_view(), name='create')
]



