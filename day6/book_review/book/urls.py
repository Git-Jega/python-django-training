from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book, name='book'),
    path('book/add/', views.add_book, name='add_book')
]
