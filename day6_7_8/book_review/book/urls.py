from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('add/', views.add_book, name='add_book'),
    path('review/<int:book_id>/', views.review_book, name='review_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
