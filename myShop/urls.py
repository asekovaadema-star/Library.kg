from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_view),
    path('categories/<int:id>/', views.category_detail_view),
]