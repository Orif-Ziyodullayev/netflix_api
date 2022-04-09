from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from netflix_2.serializers import ActorSerializers, MovieSerializers, MovieActorSerializers, CommentSerializers
from .models import Movie, Actor, Comment
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class MovieViewSet(ModelViewSet):
    actor = ActorViewSet()
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'year', 'imdb', 'actor__name']
    ordering_fields = ['imdb']
    filterset_fields = ['genre']

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get.object()
        serializer = ActorSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            actor = Actor.objects.create(
                name=data['name'],
                birthdate=data['birthdate'],
                gender=data['gender'],
                movie=data['movie'],
            )
            movie.actor.add(actor)
            movie.save()
            return Response({'status': 'The actor successfully joined'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get.object()
        serializer = ActorSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            actor = Actor.objects.get(
                name=data['name'],
                birthdate=data['birthdate'],
                gender=data['gender'],
                movie=data['movie'],
            )
        movie.actor.delete(actor)
        movie.save()
        return Response({'status': 'The actor removed'})

# class MovieActorAPIView(APIView):
#   def get(self,request,id):
#      movie = Movie.objects.filter(actor=id)
#     serializer = MovieActorSerializers(movie,many=True)
#    return Response({'movie':serializer.data})

# class CommentAPICreate(generics.CreateAPIView):
#   queryset = Comment.objects.all()
#  serializer_class = CommentSerializers
# authentication_classes = (TokenAuthentication, )
# permission_classes = (IsAuthenticated, )

# class CommentAPIList(generics.ListAPIView):
#   queryset = Comment.objects.all()
#  serializer_class = CommentSerializers
# authentication_classes = (TokenAuthentication, )
# permission_classes = (IsAuthenticated, )


# class CommentAPIDelete(generics.RetrieveDestroyAPIView):
#   queryset = Comment.objects.all()
#  serializer_class = CommentSerializers
# authentication_classes = (TokenAuthentication, )
# permission_classes = (IsAuthenticated, )
# Create your views here.
