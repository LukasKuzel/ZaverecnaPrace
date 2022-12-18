from django.urls import path
from . import views
from .views import edit_view, edit_password_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('edit/', views.edit_view, name='edit'),
    path('profile/', views.profile_detail, name='profile'),
    path('edit/', edit_view.as_view(), name='edit'),
    path('password/', edit_password_view.as_view(), name='password'),
    path('review/<int:book_id>/', views.submitReview, name='review')
]