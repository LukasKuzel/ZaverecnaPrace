from django.urls import path
from . import views

urlpatterns = [
    path('registerlist/', views.register_view, name='registerlist'),
    path('loginlist/', views.login_view, name='loginlist'),

]