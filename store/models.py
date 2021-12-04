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
    INPUT = 'I'
    OUTPUT = 'O'
    TYPE_CHOICES = [
        (INPUT, 'In'),
        (OUTPUT, 'Out')
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    observation = models.CharField(max_length=300)
    user = models.IntegerField(null=True, blank=True)

    @property
    def total(self):
        return sum(round(x.quantity * x.price)  for x in self.orderdetail_set.all())

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
