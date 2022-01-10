from django.shortcuts import render
from . import models
# Create your views here.
def my_books(request):
    post = models.my_book1.objects.all()
    return render(request,'book_list.html',{'post': post})