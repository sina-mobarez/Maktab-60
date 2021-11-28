from django.db import models

# Create your models here.

class Card(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=("product in card"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'


class Transaction(models.Model):
    Paid = 'PD'
    Awaiting = 'AW'
    Failed = 'FL'
    CHOICES = [(Paid, 'paid'),(Awaiting, 'awaiting'),(Failed, 'failed')]
    status_payment = models.CharField(max_length=2,choices= CHOICES)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    bayer = models.ForeignKey("user.Buyer", on_delete=models.CASCADE)
    date = models.DateTimeField('date of happend', auto_now=False, auto_now_add=True)
    

    def __str__(self):
        return f'{self.bayer} {self.status_payment}'
