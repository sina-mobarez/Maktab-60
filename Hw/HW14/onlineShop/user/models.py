from django.db import models

# Create your models here.

class User(models.Model):
    MALE = 'ML'
    FEMALE = 'FL'
    NOTSET = 'NT'
    GENDER_CHOICES = [(MALE, 'male'),(FEMALE, 'female'),(NOTSET, 'notset')]
    name = models.CharField('name of user', max_length=50)
    address = models.CharField('address of user', max_length=600)
    email = models.EmailField('email of user', max_length=254)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    phone_number = models.CharField('phone_number', max_length=14, unique=True)
    card = models.ForeignKey("trade.Card", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('date who user joined', auto_now_add=True)
    favorite = models.ForeignKey("feature.Favorite", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.email}'

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey("trade.Card", verbose_name=("card's user"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
