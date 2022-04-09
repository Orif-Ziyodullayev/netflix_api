from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50, null=True)
    birthdate = models.DateField(max_length=8)
    MALE = 'male'
    FEMALE = 'female'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER)

    class Meta():
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField(max_length=8)
    imdb = models.FloatField(max_length=2)
    FANTASY = 'fantasy'
    ACTION = 'action'
    DRAMA = 'drama'
    COMEDY = 'comedy'
    HORROR = 'horror'
    HISTORICAL = 'historical'
    DETECTIVE = 'detective'
    GENRES = [
        (FANTASY, 'Fantasy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
        (COMEDY, 'Comedy'),
        (HORROR, 'Horror'),
        (HISTORICAL, 'Historical'),
        (DETECTIVE, "Detective")
    ]
    genre = models.CharField(max_length=10, choices=GENRES)
    actor = models.OneToOneField(Actor, on_delete=models.CASCADE, blank=True, null=True)

    class Meta():
        ordering = ["id", "name"]

    def __str__(self):
        return f"{self.name}"


User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_id')
    text = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)