from django.urls import path
from . import views

urlpatterns = [
    path('create_basket_book/', views.create_basket_book_view),
    path('basket_book_list/', views.read_basket_book_view),
    path('basket_book_list/<int:id>/update/', views.update_basket_book_view),
    path('basket_book_list/<int:id>/delete/', views.delete_basket_book_view),

]