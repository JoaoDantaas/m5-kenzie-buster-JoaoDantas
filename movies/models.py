from django.db import models

class RatingMovie(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"

class Movie(models.Model):
    title =	models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True, default=None )
    rating = models.CharField(max_length=20, null=True, choices=RatingMovie.choices, default=RatingMovie.G )
    synopsis = models.TextField(null=True, blank=True, default=None)

    user = models.ForeignKey(
    "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    movie_order = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="movies_order")

class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="order")
    order = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie_order")
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)