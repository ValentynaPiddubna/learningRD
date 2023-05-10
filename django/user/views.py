from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .pagination import UserPagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_fields = ('id', 'first_name', 'age')
    ordering_fields = ('id', 'first_name', 'age')







