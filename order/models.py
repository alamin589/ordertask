# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    product_quantities = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)  # Stores product quantities as a dictionary
    payment_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
