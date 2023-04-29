from django.db import models
from django.utils import timezone
from user.models import User
from book.models import Book

# Create your models here.


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.id} {self.book.title} ({self.user.first_name} {self.user.last_name})"


