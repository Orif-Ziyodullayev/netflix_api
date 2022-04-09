from rest_framework import serializers
from .models import Actor, Movie,Comment


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','year','imdb','genre','actor']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =("movie_id","user_id","text","created_date")