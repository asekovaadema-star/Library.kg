from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'book_lst.html'
    context_object_name = 'book_lst'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(titile__icontains=self.request.Get.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context

# def search_view(request):
#     query = request.GET.get('s', '')
#     if query:
#        query_lst = models.Book.objects.filter(title__icontains=query)
#     else:
#         return HttpResponse('книга не найдена')
#     return render(request, 'book_lst.html', {'book_lst': query_lst})

from django.db.models import F

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'
    model = models.Book

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_book = request.session.get('viewed_book', [])

        if obj.pk not in views_book:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_book.append(obj.pk)
            request.session['viewed_blog'] = views_book
            obj.refresh_from_db()
        return obj

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Book, id=id)
#         views_book = request.session.get('viewd_book', [])

#         if id not in views_book:
#             book_id.views = F('views') + 1
#             book_id.save()
#             book_id.refresh_from_db()
#         views_book.append(id)
#         request.session['viewd_book'] = views_book
#     return render(request, 'book_detail.html', {'book_id': book_id})

class BookListView(generic.ListView):
    template_name = 'book_lst.html'
    model = models.Book
    paginate_by = 1
    ordering = ['-id']
    context_object_name = 'book_lst'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_lst'] = context['page_obj']
        return context

# def book_list_view(request):
#     if request.method == 'GET':
#         book_lst = models.Book.objects.all().order_by('-id')
#         paginator = Paginator(book_lst, 1)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
#     return render(request, 'book_lst.html', {'book_lst': page_obj})

class FavoriteBookView(generic.View):
    def get(self, request):
        return HttpResponse('the knight living only one day')

class AboutView(generic.View):
    def get(self, request):
        return HttpResponse('My dream is to live happy ever after')

class FavoriteAnimalView(generic.View):
    def get(self, request):
        return HttpResponse('My favorite animal is cat')

# def my_favorite_book(request):
#     if request.method == 'GET':
#         return HttpResponse('the knight living only one day')

# def about_myself(request):
#     if request.method == 'GET':
#         return HttpResponse('My dream is to live happy ever after')

# def favorite_animal(request):
#     if request.method == 'GET':
#         return HttpResponse('My favorite animal is cat')

