from django.test import TestCase
from rest_framework.test import APIRequestFactory
from user.models import User
from user.views import UserViewSet


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            age=30
        )
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.age, 30)

class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25
        }

    def test_create_user(self):
        request = self.factory.post('/users/', self.user_data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.age, 25)

    # def test_get_user(self):
    #     user = User.objects.create(first_name='Jane1', last_name='Smith1', age=30)
    #     request = self.factory.get(f'/users/{user.id}/')
    #     response = self.view(request, pk=user.id)
    #     data = response.data['results'][0]
    #     print(f"Response data: {data}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['first_name'], 'Jane1')
    #     self.assertEqual(response.data['last_name'], 'Smith1')
    #     self.assertEqual(response.data['age'], 30)

    def test_get_user(self):
        user = User.objects.create(first_name='Jane1', last_name='Smith1', age=30)
        request = self.factory.get(f'/users/{user.id}/')
        response = self.view(request, pk=user.id)
        data = response.data['results'][0]  # Access the first user from the results list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['first_name'], 'Jane1')
        self.assertEqual(data['last_name'], 'Smith1')
        self.assertEqual(data['age'], 30)

    def test_delete_user(self):
        user = User.objects.create(first_name='Jane1', last_name='Smith1', age=30)
        request = self.factory.delete(f'/users/{user.id}/')
        response = self.view(request, pk=user.id)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 0)
