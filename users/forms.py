from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

GENDER = (
        ("M", "M"),
        ("Ж", "Ж")
    )
class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, initial='+996')
    gender = forms.ChoiceField(choices=GENDER, required=True)
    age = forms.IntegerField(required=True)
    city = forms.CharField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    captcha = CaptchaField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username', 
            'password1',
            'password2',
            'photo',
            'first_name',
            'email',
            'phone_number',
            'gender',
            'age',
            'city',
            'bio',
        )
    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
