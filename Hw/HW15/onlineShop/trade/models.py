from django.db import models
from django.db.models.fields import related

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey("user.Buyer", on_delete=models.CASCADE)
    order_num = models.CharField(max_length=10)
    order_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.customer}'
    

class OrderItem(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} {self.order}'

class Transaction(models.Model):
    Paid = 'PD'
    Awaiting = 'AW'
    Failed = 'FL'
    CHOICES = [(Paid, 'paid'),(Awaiting, 'awaiting'),(Failed, 'failed')]
    status_payment = models.CharField(max_length=2,choices= CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_paid')
    date = models.DateTimeField('date of happend', auto_now=False, auto_now_add=True)
    

    def __str__(self):
        return f'{self.status_payment} {self.order}'
