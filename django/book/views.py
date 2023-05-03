from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
import json
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')


# # Create your views here.
# def book_list(request):
#     books = Book.objects.all()
#     book_list = list(books.values())
#     return JsonResponse(book_list, safe=False)
