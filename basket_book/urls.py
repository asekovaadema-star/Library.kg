from django.urls import path
from . import views

urlpatterns = [
    path('create_basket_book/', views.CreateBasketBoookView.as_view()),
    path('basket_book_list/', views.ReadBasketBookView.as_view()),
    path('basket_book_list/<int:id>/update/', views.UpdateBasketBookView.as_view()),
    path('basket_book_list/<int:id>/delete/', views.DeleteBasketBookView.as_view()),
    path('basket_book_list/<int:id>/',views.DetailBasketBoookView.as_view()),
]