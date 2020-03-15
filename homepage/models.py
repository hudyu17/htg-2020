from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25, default="")
    store = models.CharField(max_length=25, default="")
    location = models.CharField(max_length=25, default="")
    longitude = models.DecimalField(max_digits=19, decimal_places=10, default="-79")
    latitude = models.DecimalField(max_digits=19, decimal_places=10, default="43")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    #longitude = models.CharField(max_length=25, default="-79")
    #latitude = models.CharField(max_length=25, default="43")

    def __str__(self):
        return self.name
