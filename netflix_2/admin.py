
from django.contrib import admin
from .models import Movie, Actor, Comment


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'imdb', 'actor')
    list_display_links = ('name', 'year', 'actor')
    list_filter = ('year', 'imdb', 'genre', 'actor')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'gender')
    list_filter = ('gender', 'movie')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'user_id', 'created_date']


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
