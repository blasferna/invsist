from django.db import models
from inventory.models import Product

class Buyer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    addres = models.CharField(max_length=500, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    addres = models.CharField(max_length=500, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    suppier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    observation = models.CharField(max_length=300)
    user = models.IntegerField()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)