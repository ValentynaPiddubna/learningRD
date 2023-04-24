"""
URL configuration for robot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from user import views
from user.views import user_list
from book.views import book_list
from purchase.views import purchase_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list, name='user_list'),
    path('books/', book_list, name='book_list'),
    path('purchases/', purchase_list, name='purchase_list'),

]
