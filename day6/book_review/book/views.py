from django.shortcuts import render
from .models import Book

def book(request):
  books = Book.objects.all()
  # books = Book.objects.order_by("title")
  return render(request,"book.html",{'books' : books})
  # return HttpResponse("<h1>hello from book</h1>")

def add(request):
  val1 = request.GET['num1']
  val2 = request.GET['num2']
  result = int(val1)+int(val2)
  return render(request,"result.html",{'result':result})