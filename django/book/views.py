from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ("title", "author", "year")
    ordering_fields = ('title', 'author', 'year')




