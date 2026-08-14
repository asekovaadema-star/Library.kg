from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic


class CategoryListView(generic.ListView):
    model = models.Categories
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(generic.DetailView):
    model = models.Categories
    template_name = 'category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = models.Products.objects.filter(product_categories_id=self.object.id)
        return context

# def category_detail_view(request, id):
#     if request.method == 'GET':
#         category = get_object_or_404(models.Categories, id=id)
#         products = models.Products.objects.filter(product_categories_id=id)
#         return render(request, 'category_detail.html', {
#             'category': category,
#             'products': products})

# def category_list_view(request):
#     if request.method == 'GET':
#         categories = models.Categories.objects.all()
#         return render(request, 'category_list.html', {'categories': categories})
