from django.shortcuts import render
from .temp_data import movie_data

def index(request):
    context = {}
    return render(request, 'movies/index.html', context)

def about(request):
    context = {}
    return render(request, 'movies/about.html', context)

def detail(request, movie_id):
    context = {'movie': movie_data[movie_id - 1]}
    return render(request, 'movies/detail.html', context)

