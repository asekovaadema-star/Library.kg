from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#many to many
class CategoryHorse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(CategoryHorse, null=True)

    def __str__(self):
        return f'{self.title} - {', '.join(i.name for i in self.categories.all())}'

#one to one
class Reservation(models.Model):
    location_title = models.OneToOneField(Location, on_delete=models.CASCADE)
    personal_number = models.CharField(max_length=10, default='996_____')
    

    def __str__(self):
        return f'{self.personal_number} - {self.location_title}'

#one to many
class CommentLocation(models.Model):
    choice_location= models.ForeignKey(Location, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default = 5, 
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_location} - {self.mark}'
