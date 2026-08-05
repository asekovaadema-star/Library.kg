from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def create_basket_book_view(request):
    if request.method == 'POST':
        form_obj = forms.BasketForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/basket_book_list/')
    else:
        form_obj = forms.BasketForm()
    return render(request, 'create_basket_book.html', {'form':form_obj})

def read_basket_book_view(request):
    if request.method == 'GET':
        basket_book_list = models.BasketBook.objects.all()
    return render(request, 'read_basket_book.html', {'basket_book_list': basket_book_list})

def update_basket_book_view(request, id):
    basket_book_id = get_object_or_404(models.BasketBook, id=id)
    if request.method == 'POST':
        form_obj = forms.BasketForm(request.POST, instance=basket_book_id)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/basket_book_list/')
    else:
        form_obj = forms.BasketForm(instance=basket_book_id)
    return render(request, 'update_basket_book.html', {'form':form_obj, 'basket_book_id': basket_book_id})

def delete_basket_book_view(request, id):
    basket_book_id = get_object_or_404(models.BasketBook, id=id)
    basket_book_id.delete()
    return redirect('/basket_book_list/')



