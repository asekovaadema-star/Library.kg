from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator


def search_view(request):
    query = request.GET.get('s', '')
    if query:
       query_lst = models.Book.objects.filter(title__icontains=query)
    else:
        return HttpResponse('книга не найдена')
    return render(request, 'book_lst.html', {'book_lst': query_lst})

from django.db.models import F
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        views_book = request.session.get('viewd_book', [])

        if id not in views_book:
            book_id.views = F('views') + 1
            book_id.save()
            book_id.refresh_from_db()
        views_book.append(id)
        request.session['viewd_book'] = views_book
    return render(request, 'book_detail.html', {'book_id': book_id})

def book_list_view(request):
    if request.method == 'GET':
        book_lst = models.Book.objects.all().order_by('-id')
        paginator = Paginator(book_lst, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
    return render(request, 'book_lst.html', {'book_lst': page_obj})

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
