from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse



def user_list(request):
    users = User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)

