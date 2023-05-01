from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

app_name = 'purchase'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('create/', PurchaseCreateView.as_view(), name='purchase_create'),
]
