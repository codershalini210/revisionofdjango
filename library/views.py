from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def book_list(request):
    books = Book.objects.all()
    context = {"all_Books":books}
    return render(request,'library/book_list.html',context)
def about_view(request):
    return HttpResponse("<h2>About us </h2>")
# Create your views here.
def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    context = {"book":book}
    return render(request,"library/book_details.html",context)
