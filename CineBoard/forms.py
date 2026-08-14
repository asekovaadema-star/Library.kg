from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 
                  'email')

class CinemaForm(forms.ModelForm):
    class Meta:
        model = models.CinemaModel
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']

class VIPReservationForm(forms.ModelForm):
    class Meta:
        model = models.VIPReservation
        fields = ['seat_number']

