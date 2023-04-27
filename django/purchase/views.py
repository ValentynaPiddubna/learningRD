from django.shortcuts import render
from django.http import JsonResponse
from .models import Purchase
import json


# Create your views here.
def purchase_list(request):
    purchases = Purchase.objects.all()
    purchase_list = list(purchases.values())
    return JsonResponse(purchase_list, safe=False)

