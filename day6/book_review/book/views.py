from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return render(request, 'my_template.html')


def book(request):
  books = Book.objects.all()
  # books = Book.objects.order_by("title")
  return render(request,"book.html",{'books' : books})
  # return HttpResponse("<h1>hello from book</h1>")

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def add(request):
  val1 = request.GET['num1']
  val2 = request.GET['num2']
  result = int(val1)+int(val2)
  return render(request,"result.html",{'result':result})