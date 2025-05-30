from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Publicado(models.Model):
    date = models.PositiveIntegerField()
    mes = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    description = models.TextField(blank=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    nacionalidade = models.CharField(max_length=100)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
