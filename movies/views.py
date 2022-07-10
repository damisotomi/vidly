from doctest import OutputChecker
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # remember that this returns a list so we can iterate through it
    # other methods we can use are
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    # we can write the code below as a list comprehension
    # output = ''
    # for m in movies:
    #     output += m.title
    # output = ', '.join([m.title for m in movies])
    # always prefix your templates with their folder name so django doesnt go and load index file from another app
    return(render(request, 'movies/index.html', {'movies': movies}))


def detail(request, movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    # we could use pk or id
    return render(request,'movies/detail.html',{'movie':movie})