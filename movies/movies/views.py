from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from api.models import Movie
from django.urls import reverse

def list(request):
    all_movies = Movie.objects.all()   
    return render(request, 'movies.html', {'movies': all_movies})

def detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/movie.html', {'movie': movie})

def updateMovieLikesUp(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.likes+=1
    movie.save()
    return HttpResponseRedirect(reverse(list))

def updateMovieLikesDown(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.likes-=1
    movie.save()
    return HttpResponseRedirect(reverse(list))

def delete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return HttpResponseRedirect(reverse(list))