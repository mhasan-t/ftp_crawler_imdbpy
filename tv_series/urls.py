from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'tv'

urlpatterns = [
    path('', views.TVList.as_view(), name='list'),
    path('<int:pk>/', views.TVDetails.as_view(), name='details'),
    path('create/', views.TVCreate.as_view(), name='create'),
    path('create-file/', views.AddTVWithFile.as_view(), name='create-file'),
    path('auto-create/', views.TVAutoCreate.as_view(), name='auto-create'),


    path('episodes/<path:ddir>', views.episodes, name='get-eps'),


]



