from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CinemaModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField(default='2026-01-01')
    country = models.CharField(max_length=100, default='США')
    director = models.CharField(max_length=100, default='Режиссер')
    duration = models.PositiveIntegerField(default=120)
    age_limit = models.CharField(max_length=10, default='16+')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=300.00)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class VIPReservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    film = models.ForeignKey(CinemaModel, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.seat_number}"

class Comment(models.Model):
    film = models.ForeignKey(CinemaModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.film.title}"