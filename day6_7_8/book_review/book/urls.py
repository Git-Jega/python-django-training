from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('add/', views.add_book, name='add_book'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('review/<int:book_id>/', views.review_book, name='review_book'),
    path('book/<int:book_id>/restock/', views.restock_book, name='restock_book'), 
    path('book/<int:book_id>/return/', views.return_book, name='return_book'), 
    path('books/<int:book_id>/borrowers/', views.borrowers_list, name='borrowers_list'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('listreview/<int:book_id>', views.list_review, name="list_review"),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
