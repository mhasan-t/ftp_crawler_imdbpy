from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from movies.modelforms import CreateMoviesForm
from movies.models import Movies


class MovieList(ListView):
    model = Movies
    template_name = 'movie_list.html'
    queryset = Movies.objects.all()
    context_object_name = 'movies'


class MovieDetails(DetailView):
    model = Movies
    template_name = 'movie_detail.html'
    queryset = Movies.objects.all()
    context_object_name = 'movie'


class MovieCreate(CreateView):
    template_name = 'movie_create.html'
    model = Movies
    form_class = CreateMoviesForm
    queryset = Movies.objects.all()
    success_url = reverse_lazy('movie:list')


class MovieWatch(DetailView):
    model = Movies
    template_name = 'movie_watch.html'
    queryset = Movies.objects.all()
    context_object_name = 'movie'


