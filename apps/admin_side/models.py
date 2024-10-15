from django.db import models

# Create your models here.

class Size(models.Model):
    Product_size = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Product_size if self.Product_size else "No Size" 


class Product(models.Model):
    Product_name = models.CharField(max_length=225, null=True, blank=True)
    Product_colour = models.CharField(max_length=225, null=True, blank=True)
    Product_image = models.ImageField(null=True, blank=True)
    Product_size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    Product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Product_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Product_name if self.Product_name else "No Product Name"
    
    