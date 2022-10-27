from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booklist/', views.BookListView.as_view(), name='booklist'),
    path('authorlist/', views.AuthorListView.as_view(), name='authorlist'),
    path('quizlist/', views.QuizListView.as_view(), name='quizlist'),

]