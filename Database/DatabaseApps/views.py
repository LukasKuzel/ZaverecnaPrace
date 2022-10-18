from django.shortcuts import render
from django.views.generic import ListView, DetailView

from DatabaseApps.models import *

class BookListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'book/listBook.html'


def index(request):
    profile = Profile.objects.all()
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    authors = Author.objects.all()
    genres = Genre.objects.all()


    PoslatVen = {
        'profile':profile,
        'num_books':num_books,
        'books':books,
        'authors':authors,
        'genres':genres,

    }

    return render(request, 'index.html', context=PoslatVen)


