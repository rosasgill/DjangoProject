from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Antonio Gabriel

class Author(models.Model):
    name = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.name
