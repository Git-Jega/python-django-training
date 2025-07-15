from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from .forms import Review_Form
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def my_view(request):
    return render(request, 'my_template.html')

@login_required
def book(request):
  books = Book.objects.all()
  # books = Book.objects.order_by("title")
  return render(request,"book.html",{'books' : books})
  # return HttpResponse("<h1>hello from book</h1>")

@login_required
def add_book(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add(request):
  val1 = request.GET['num1']
  val2 = request.GET['num2']
  result = int(val1)+int(val2)
  return render(request,"result.html",{'result':result})

@login_required
def review_book(request, book_id):
  book = get_object_or_404(Book, id=book_id)

  if request.method == 'POST':
        form = Review_Form(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('book')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
  else:
      form = Review_Form()

  return render(request, "review_book.html", {
      "book": book,
      "form": form,
  })

@login_required
def edit_book(request, book_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('book')
    
    messages.error(request, 'Invalid request method.')
    return redirect('book')
