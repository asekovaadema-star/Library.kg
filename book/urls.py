from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_favorite_book),
    path('about/', views.about_myself),
    path('animal', views.favorite_animal)
]