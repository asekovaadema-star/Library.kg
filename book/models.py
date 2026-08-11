from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='book/')
    description = models.TextField(blank = True)
    tags = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    url_book = models.URLField(blank=True)
    type = models.CharField(max_length=20)
    views = models.PositiveIntegerField(default=0, null=True)
    state = models.CharField(max_length=20)
    created_at= models.DateField(null = True)

    def __str__(self):
        return self.title


