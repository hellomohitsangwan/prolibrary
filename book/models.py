from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000, default='No description provided')
    category = models.CharField(max_length=500, default='General')
    price = models.IntegerField()

    def __str__(self):
        return self.title
