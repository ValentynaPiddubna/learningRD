# Generated by Django 4.2 on 2023-04-24 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
    ]