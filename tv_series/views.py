
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView

from etc_files import get_tv, get_tv_file, get_seasons, get_episodes
from tv_series.modelforms import CreateTvsForm, CreateFromVideo
from tv_series.models import TV


class TVList(ListView):
    model = TV
    template_name = 'tv_list.html'
    queryset = TV.objects.all()
    context_object_name = 'tvs'


class TVDetails(DetailView):
    model = TV
    template_name = 'tv_detail.html'
    queryset = TV.objects.all()
    context_object_name = 'tv'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        tv_obj_detail = super().get_object()
        dir = tv_obj_detail.dir
        seasons = get_seasons(dir)
        data['seasons'] = seasons
        return data


class TVCreate(CreateView):
    template_name = 'tv_create.html'
    model = TV
    form_class = CreateTvsForm
    queryset = TV.objects.all()
    success_url = reverse_lazy('tv:list')


class TVAutoCreate(CreateView):
    template_name = "tv_auto.html"
    # form_class = Auto

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
        get_tv(directory)
        return redirect(reverse_lazy('tv:list'))


class AddTVWithFile(CreateView):
    template_name = "tv_create_file.html"
    # form_class = CreateFromVideo
    f = CreateFromVideo()

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context={'form': self.f})

    def post(self, request, *args, **kwargs):
        data = request.POST
        d = {}
        for key, value in data.items():
            d[key] = value

        del d['csrfmiddlewaretoken']

        dir = d['dir']
        name = d['name']
        get_tv_file(dir, name)
        return redirect(reverse_lazy('tv:list'))


def episodes(request, ddir):
    template_name = 'tv_episodes.html'
    episodes = get_episodes(ddir)
    return render(request, template_name=template_name, context={'episodes': episodes})

