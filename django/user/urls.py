from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', UserCreateView.as_view(), name='user_create'),

]
