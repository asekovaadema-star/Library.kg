from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    name_product = models.CharField(max_length=100)
    price = models.IntegerField()
    product_categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_product} - {self.price}'

# Create your models here.
