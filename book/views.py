from django.shortcuts import render
from django.http import HttpResponse

def my_favorite_book(request):
    if request.method == 'GET':
        return HttpResponse('the knight living only one day')

def about_myself(request):
    if request.method == 'GET':
        return HttpResponse('My dream is to live happy ever after')

def favorite_animal(request):
    if request.method == 'GET':
        return HttpResponse('My favorite animal is cat')

# Create your views here.
