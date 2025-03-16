from django.contrib import admin # type: ignore
from .models import Category, Genre, Movie, Movieshots, Actor, Rating, RatingStar, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movieshots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
