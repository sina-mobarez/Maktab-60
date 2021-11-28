from django.db import models
from user.models import User
# Create your models here.

class Favorite(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

class Comment(models.Model):
    content = models.CharField('text of commnet', max_length=120)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}'
        


class Email(models.Model):
    caption = models.CharField(max_length=50)
    content = models.TextField()
    related_transaction = models.ForeignKey("trade.Transaction", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
