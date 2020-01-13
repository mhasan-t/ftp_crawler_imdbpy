import os
from io import BytesIO
from time import sleep
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from pytz import unicode

from movies.modelforms import CreateMoviesForm, Auto
from movies.models import Movies

from etc_files import read_url, take_name, getMovieDatabyName, getMovieDatabyID, get_movie


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




class MovieAutoCreate(CreateView):
    template_name = "movie_auto.html"
    form_class = Auto

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        print("CRAWLING")
        data = request.POST
        d = {}
        for key, value in data.items():
            d[key] = value

        del d['csrfmiddlewaretoken']

        directory = d["directory"]
        get_movie(directory)
        return redirect(reverse_lazy('movie:list'))



