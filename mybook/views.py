from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse 
from .models import mybook, Author
from .forms import BookForm, AuthorForm

def index(request):
    books = mybook.objects.all()
    return render(request, 'mybook/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(mybook, pk=book_id)
    return render(request, 'mybook/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'mybook/add_book.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'mybook/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'mybook/author_detail.html', {'author': author})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'mybook/add_author.html', {'form': form})

def book_list(request):
    books = mybook.objects.all()
    return render(request, 'mybook/book_list.html', {'books': books})



from rest_framework import viewsets
from .models import Author, mybook
from .serializers import AuthorSerializer, mybookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class mybookViewSet(viewsets.ModelViewSet):
    queryset = mybook.objects.all()
    serializer_class = mybookSerializer



