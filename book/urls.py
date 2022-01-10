from django.urls import path
from . import views
urlpatterns = [
    path('mybooks/', views.my_books, name='mybooks'),
]