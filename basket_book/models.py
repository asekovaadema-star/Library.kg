from django.db import models
from book.models import Book
from django import forms
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

card_regex = RegexValidator(
    regex=r'^\d{16}$',
    message='Номер карты должен состоять ровно из 16 цифр.'
)

class BasketBook(models.Model):
    name_order = models.CharField(max_length=20)
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, 
                                        validators=
                                        [MinValueValidator(1),
                                        MaxValueValidator(5)])
    card_number = models.CharField(
        max_length=16,
        validators=[card_regex])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS = (
        ('доставлено', "доставлено"),
        ("в пути", "в пути"),
        ("отменено", "отменено")
    )
    status = models.CharField(max_length=100, choices=STATUS)

    
    

