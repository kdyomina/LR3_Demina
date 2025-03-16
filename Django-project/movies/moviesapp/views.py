from django.shortcuts import render # type: ignore
from django.views.generic.base import View # type: ignore
from .models import Movie

class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "Django-project/movies/templates/moviesapp/movie_list.html", {"movie_list": movies})

