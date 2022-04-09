from django.test import TestCase,Client
from netflix_2.models import Movie,Actor

# Create your tests here.
class TestMovieImdb(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.bulk_create(
            [Movie
             (name='Thor',year='2022-3-25',imdb='8',genre='fantasy'),
             Movie
             (name='Split',year='2022-3-26',imdb='9',genre='action')
             ]
        )

        self.client = Client()
        self.movie_all = Movie.objects.all()

    def test_ordering_movie(self):
        response = self.client.get('/movies/?ordering=imdb')
        replica = Movie.objects.all()
        data = response.data
        self.assertEquals(len(data),2)
        self.assertEquals(data[0]['imdb'],8)
        self.assertEqual(response.status_code,200)

