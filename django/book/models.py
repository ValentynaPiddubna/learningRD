from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.FloatField()

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title
