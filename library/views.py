from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    context = {"all_Books":books}
    return render(request,'library/book_list.html',context)
# Create your views here.
