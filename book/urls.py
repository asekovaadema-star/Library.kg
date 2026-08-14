from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.FavoriteBookView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('animal/', views.FavoriteAnimalView.as_view),
    path('book_list/', views.BookListView.as_view()),
    path('book_list/<int:id>/', views.BookDetailView.as_view()),
    path('search/', views.SearchView.as_view()),
]