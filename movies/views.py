from django.shortcuts import render

# Create your views here.
from movies.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request,'movies.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request,'movies/movie_detail.html', {'movie': movies})
