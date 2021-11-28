from django.db import models

# Create your models here.

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= 'AVL')

class UnavailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= 'UVL')

class Section(models.Model):
    name = models.CharField('name of section', max_length=50)

    def __str__(self):
        return f'{self.name}'    

class Catagory(models.Model):
    name = models.CharField('name of catagory', max_length=50)
    section = models.ForeignKey(Section, verbose_name=("section of catagories"), on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'    

class Product(models.Model):
    AVAILABLE= 'AVL'
    UNAVAILABLE= 'UVL'
    NOTSET= 'NOT'
    STATUS= [
        (AVAILABLE, 'available'),
        (UNAVAILABLE, 'unavailable'),
        (NOTSET, 'not set')
    ]
    name = models.CharField("name of product", max_length=50)
    desc = models.TextField('description')
    unit = models.CharField('unit of product', max_length=25)
    status= models.CharField('status of availiblity of product', max_length=3, choices=STATUS)
    price_per_unit = models.DecimalField('price of one of product', max_digits=14, decimal_places=2)
    catagory = models.ForeignKey(Catagory, verbose_name=("catagory of product"),null=True , on_delete=models.SET_NULL)
    owner = models.ForeignKey("user.Seller", on_delete=models.CASCADE)
    tags = models.ManyToManyField("feature.Tag", blank=True)
    objects= models.Manager()
    available= AvailableManager()
    unavailable= UnavailableManager()

    class Meta:
        ordering = ['name']


    def __str__(self):
        return f'{self.name} {self.catagory}'
