from django.shortcuts import render,get_object_or_404,redirect
from .models import Book, Review, BorrowedBook
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from .forms import Review_Form
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.db import transaction

@login_required
def my_view(request):
    return render(request, 'my_template.html')

@login_required
def book(request):
    if request.user.is_superuser:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(borrowedbook__user=request.user)
  # books = Book.objects.order_by("title")
    return render(request,"book.html",{'books' : books})
  # return HttpResponse("<h1>hello from book</h1>")

@login_required
def add_book(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    if request.method == 'POST':
        form = BookForm(request.POST)
        form.fields.pop('rating')
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
    else:
        form = BookForm()
        form.fields.pop('rating')
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
def borrow_book(request):
    books = Book.objects.filter(copies__gt=0)
    borrow_success = None
    error_message = ""
    selected_book = None

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        try:
            selected_book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            error_message = "Book not found."
        else:
            already_borrowed = BorrowedBook.objects.filter(book=selected_book, user=request.user).exists()

            if already_borrowed:
                error_message = "You've already borrowed this book."
            else:
                with transaction.atomic():
                    selected_book = Book.objects.select_for_update().get(id=book_id)

                    if selected_book.copies <= 0:
                        error_message = "No copies left to borrow."
                    else:
                        selected_book.copies -= 1
                        selected_book.save()

                        BorrowedBook.objects.create(user=request.user, book=selected_book)
                        borrow_success = True

    return render(request, "borrow_book.html", {
        "books": books,
        "borrow_success": borrow_success,
        "error_message": error_message,
        "selected_book": selected_book
    })


@login_required
def list_review(request, book_id):
    reviews = Review.objects.filter(book_id=book_id,user_id=request.user.id)
    book = Book.objects.get(id = book_id)
    return render(request,"list_review.html",{'reviews' : reviews,'book': book.title})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == "POST":
        form = Review_Form(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('list_review', book_id=review.book.id)
    else:
        form = Review_Form(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def edit_book(request, book_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
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

@login_required
def restock_book(request, book_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        try:
            copies = int(request.POST.get("copies", 0))
            if copies > 0:
                book.copies += copies
                book.save()
                messages.success(request, f"{copies} copies added to '{book.title}'.")
            else:
                messages.error(request, "Please enter a positive number.")
        except ValueError:
            messages.error(request, "Invalid number format.")
        
        return redirect('book')

    messages.error(request, "Invalid request method.")
    return redirect('book')

@login_required
def borrowers_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to view the borrowers list.")

    borrowers = BorrowedBook.objects.filter(book=book).select_related('user')

    context = {
        'book': book,
        'borrowers': borrowers,
    }

    return render(request, 'borrowers_list.html', context)

@login_required
def return_book(request, book_id):    
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.copies += 1
        book.save()
        borrowed = BorrowedBook.objects.filter(user=request.user, book=book).first()
        if borrowed:
            borrowed.delete()
        messages.success(request, f"'{book.title}' returned successfully.")        
        return redirect('book')
    messages.error(request, "Book return failed.")
    return redirect('book')

@login_required
def delete_review(request,review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    book_id = review.book.id
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('list_review', book_id=book_id)
    
    messages.error(request, 'Invalid request method.')
    return redirect('list_review', book_id=book_id)
