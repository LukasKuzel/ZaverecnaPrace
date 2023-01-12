from django.db.models import Avg, Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from DatabaseApps.models import *


class BookListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'page/listBook.html'

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Book.objects.filter(genre__name=self.kwargs['genre_name']).all()
        elif 'century_name' in self.kwargs:
            return Book.objects.filter(century__name=self.kwargs['century_name']).all()
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'genre_name' in self.kwargs:
            context['view_title'] = f"ŽÁNR: {self.kwargs['genre_name']}"
            context['view_head'] = f"ŽÁNR KNIH: {self.kwargs['genre_name']}"
        elif 'century_name' in self.kwargs:
            context['view_title'] = f"STOLETÍ: {self.kwargs['century_name']}"
            context['view_head'] = f"STOLETÍ: {self.kwargs['century_name']}"
        else:
            context['view_title'] = 'KNIHY'
            context['view_head'] = 'SEZNAM KNIH'
        return context

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

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Book.objects.filter(genre__name=self.kwargs['genre_name']).all()
        elif 'century_name' in self.kwargs:
            return Book.objects.filter(century__name=self.kwargs['century_name']).all()
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review5'] = Review.objects.all().filter(book__id=self.kwargs['pk'], status=True)
        context['aggregates'] = Review.objects.all().filter(book__id=self.kwargs['pk']).aggregate(Avg('rate'))
        if 'genre_name' in self.kwargs:
            context['view_title'] = f"ŽÁNR: {self.kwargs['genre_name']}"
            context['view_head'] = f"ŽÁNR KNIH: {self.kwargs['genre_name']}"
        elif 'century_name' in self.kwargs:
            context['view_title'] = f"STOLETÍ: {self.kwargs['century_name']}"
        else:
            context['view_title'] = 'KNIHY'
            context['view_head'] = 'SEZNAM KNIH'
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'authors_detail'
    template_name = 'page/detailAuthor.html'


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        queryset1 = Author.objects.annotate(fullname=Concat('name', Value(' '), 'surname'))
        resultA = queryset1.filter(fullname__icontains=searched) | Author.objects.filter(
            name__iexact=searched) | Author.objects.filter(surname__iexact=searched) | Author.objects.filter(
            name__istartswith=searched) | Author.objects.filter(surname__istartswith=searched)
        resultB = Book.objects.filter(name__contains=searched) | Book.objects.filter(
            name__iexact=searched) | Book.objects.filter(name__istartswith=searched) | Book.objects.filter(
            century__name__icontains=searched)

        PoslatVen = {
            'searched':searched,
            'resultA':resultA,
            'resultB':resultB,
        }

        return render(request, 'page/search_bar.html', context=PoslatVen)
    else:
        return render(request, 'page/search_bar.html', {})

def index(request):
    century = Century.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    nation = Nation.objects.all()


    PoslatVen = {
        'century':century,
        'books':books,
        'authors':authors,
        'genres':genres,
        'nation':nation,
    }

    return render(request, 'index.html', context=PoslatVen)




