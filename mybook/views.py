from django.shortcuts import render, redirect
from .models import mybook, Author
from .forms import BookForm, AuthorForm

def index(request):
    books = mybook.objects.all()
    authors = Author.objects.all()
    return render(request, 'mybook/index.html', {'books': books, 'authors': authors})

def book_detail(request, book_id):
    book = mybook.objects.get(pk=book_id)
    return render(request, 'mybook/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mybook:index')
    else:
        form = BookForm()
    return render(request, 'mybook/add_book.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'mybook/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'mybook/author_detail.html', {'author': author})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mybook:index')
    else:
        form = AuthorForm()
    return render(request, 'mybook/add_author.html', {'form': form})

def book_list(request):
    books = mybook.objects.all()
    return render(request, 'mybook/book_list.html', {'books': books})


def index(request):
    books = mybook.objects.all()
    return render(request, 'mybook/index.html', {'books': books})
