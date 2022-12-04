from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'movies/index.html', context)

def about(request):
    context = {}
    return render(request, 'movies/about.html', context)
