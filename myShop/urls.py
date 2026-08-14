from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailView.as_view()),
]