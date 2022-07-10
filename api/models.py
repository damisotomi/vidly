from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        # the resource_name is basically where other applications will find your movie data prefixed by api
        excludes = ['date_created']
