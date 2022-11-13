from django.shortcuts import render
from django.views.generic import ListView, DetailView

from DatabaseApps.models import *


class BookListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'page/listBook.html'


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors_list'
    template_name = 'page/listAuthor.html'


class QuizListView(ListView):
    model = Author
    context_object_name = 'quiz_list'
    template_name = 'page/listQuiz.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'books_detail'
    template_name = 'page/detailBook.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'authors_detail'
    template_name = 'page/detailAuthor.html'


class AuthorHasBook(DetailView):
    model = AuthorHasBook
    context_object_name = 'author_has_book'


def index(request):
    profile = Profile.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    quizs = Quiz.objects.all()


    PoslatVen = {
        'profile':profile,
        'books':books,
        'authors':authors,
        'genres':genres,
        'quizs':quizs,

    }

    return render(request, 'index.html', context=PoslatVen)


