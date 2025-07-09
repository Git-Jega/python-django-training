from django.urls import path
from . import views

urlpatterns = [
    path('myworld/', views.myworld),
]