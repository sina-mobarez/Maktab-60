from django.db import models
from user.models import User
# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_fav')
    name = models.CharField('a name for your fav list', max_length=50)

    def __str__(self):
        return f'{self.name} fav list'

class FavoriteItem(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name='user_fav_product')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'    

class CommonInfo(models.Model):
    content = models.CharField('text of commnet', max_length=120)

    class Meta:
        abstract = True
        ordering = ['content']

class Comment(CommonInfo):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.author}'
        


class Email(CommonInfo):
    caption = models.CharField(max_length=50)
    content = models.TextField()
    related_transaction = models.ForeignKey("trade.Transaction", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Tag(models.Model):
    name= models.CharField('start with #', max_length=50)

    def __str__(self):
        return self.name
