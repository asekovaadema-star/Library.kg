from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

class CreateBasketBoookView(generic.CreateView):
    template_name = 'create_basket_book.html'
    form_class = forms.BasketForm
    success_url = '/basket_book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketBoookView, self).form_valid(form=form)
    
# def create_basket_book_view(request):
#     if request.method == 'POST':
#         form_obj = forms.BasketForm(request.POST)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/basket_book_list/')
#     else:
#         form_obj = forms.BasketForm()
#     return render(request, 'create_basket_book.html', {'form':form_obj})

class ReadBasketBookView(generic.ListView):
    template_name ='read_basket_book.html'
    model = models.BasketBook
    context_object_name = 'basket_book_list'

    def get_queryset(self):
        return self.model.objects.all()


class DetailBasketBoookView(generic.DetailView):
    template_name = 'basket_book_detail.html'
    context_object_name = 'basket_book_id'

    def get_object(self, **kwargs):
        basket_book_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketBook, id=basket_book_id)

# def read_basket_book_view(request):
#     if request.method == 'GET':
#         basket_book_list = models.BasketBook.objects.all()
#     return render(request, 'read_basket_book.html', {'basket_book_list': basket_book_list})

class UpdateBasketBookView(generic.UpdateView):
    template_name = 'update_basket_book.html'
    form_class = forms.BasketForm
    success_url = '/basket_book_list/'
    context_object_name =  'basket_book_id'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketBookView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        basket_book_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketBook, id=basket_book_id)

# def update_basket_book_view(request, id):
#     basket_book_id = get_object_or_404(models.BasketBook, id=id)
#     if request.method == 'POST':
#         form_obj = forms.BasketForm(request.POST, instance=basket_book_id)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/basket_book_list/')
#     else:
#         form_obj = forms.BasketForm(instance=basket_book_id)
#     return render(request, 'update_basket_book.html', {'form':form_obj, 'basket_book_id': basket_book_id})

class DeleteBasketBookView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'basket_book_id'
    success_url = '/basket_book_list/'

    def get_object(self, **kwargs):
        basket_book_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketBook, id=basket_book_id)

# def delete_basket_book_view(request, id):
#     basket_book_id = get_object_or_404(models.BasketBook, id=id)
#     basket_book_id.delete()
#     return redirect('/basket_book_list/')



