from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('user_list')

