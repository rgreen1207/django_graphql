from django.shortcuts import render
from django.http import Http404
from api.models import Movie

def list(request):
    all_movies = Movie.objects.all()
    print(all_movies)
    return render(request, 'movies.html', {'movies': all_movies})


def detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/movie.html', {'movie': movie})