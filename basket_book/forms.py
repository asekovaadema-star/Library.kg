from django import forms
from . import models

class BasketForm(forms.ModelForm):
    class Meta:
        model = models.BasketBook
        fields = '__all__'