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
from django.urls import include, path
from user.views import UserListView, UserDetailView
from book.views import BookListView, BookDetailView
from purchase.views import PurchaseListView, PurchaseDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    # path('users/', user_list, name='user_list'),
    # path('books/', book_list, name='book_list'),
    path('books/', include('book.urls')),
    # path('purchases/', purchase_list, name='purchase_list'),
    path('purchases/', include('purchase.urls')),


]
