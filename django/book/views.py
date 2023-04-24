from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
import json


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    book_list = list(books.values())
    return JsonResponse(book_list, safe=False)
