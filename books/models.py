from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"Книги"



class Genre(models.Model):
    title = models.CharField(max_length=50)

