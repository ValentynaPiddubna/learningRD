from django.shortcuts import render
from django.http import JsonResponse
from .models import Purchase
import json
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy



class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'purchase'
    ordering = ['-date']
    # paginate_by = None


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'
    context_object_name = 'purchase'


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchase_form.html'
    fields = '__all__'
    success_url = reverse_lazy('purchase:purchase_list')


