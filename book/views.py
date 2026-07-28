from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})

def book_list_view(request):
    if request.method == 'GET':
        book_lst = models.Book.objects.all().order_by('-id')
    return render(request, 'book_lst.html', {'blog_lst': book_lst})

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
