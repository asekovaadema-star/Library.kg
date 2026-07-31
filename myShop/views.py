from django.shortcuts import render, get_object_or_404
from . import models

def category_detail_view(request, id):
    if request.method == 'GET':
        category = get_object_or_404(models.Categories, id=id)
        products = models.Products.objects.filter(product_categories_id=id)
        return render(request, 'category_detail.html', {
            'category': category,
            'products': products})

def category_list_view(request):
    if request.method == 'GET':
        categories = models.Categories.objects.all()
        return render(request, 'category_list.html', {'categories': categories})
