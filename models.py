from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    content = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    content = models.TextField()
