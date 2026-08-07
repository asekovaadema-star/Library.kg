from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(User):
    photo = models.ImageField(upload_to='users/', blank=True)
    phone_number = models.CharField(max_length=15)
    GENDER = (
        ("M", "M"),
        ("Ж", "Ж")
    )
    gender = models.CharField(max_length=100, choices=GENDER, default="M")
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(12), MaxValueValidator(100)]
    )
    city = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True, verbose_name="О себе")
    def __str__(self):
        return self.username