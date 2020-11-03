from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    book_object = Book.objects.all()
    return render(request, 'bookapp/book_list.html', {'book_object': book_object})
