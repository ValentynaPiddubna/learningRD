from celery import shared_task
# from django.contrib.auth import get_user_model
from purchase.models import Purchase
from user.models import User

# User = get_user_model()


@shared_task
def my_task():
    print('celery test')

@shared_task
def print_text(text):
    print(text)


@shared_task
def print_user_purchase_count(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = Purchase.objects.filter(user=user).count()
    print(f"User {user.first_name} has {purchase_count} purchases.")


@shared_task
def print_users_count():
    user_count = User.objects.count()
    print(f"There are {user_count} users in the database.")
