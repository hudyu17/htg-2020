from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25, default="")
    store = models.CharField(max_length=25, default="")
    location = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.name