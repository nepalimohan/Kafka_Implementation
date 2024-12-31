from django.db import models
from product.producers import send_product_data


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(self)
        send_product_data(self)