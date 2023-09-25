from typing import Any
from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    Categories = [
        # In admin panel, in db
        ('Phone','Phone'),
        ('laptop','laptop'),
        ('pc','pc'),
    ]
    name = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    # price = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=Categories, null=True, blank=True)
    added_date = models.DateField(verbose_name='Added Date', default=timezone.now())
    # time = models.TimeField()
    # created = models.DateTimeField()



    def __str__(self):
        # to change the ovjects name to it is real name
        return self.name
    
    # class Meta:
        # ordering = ['-price']
        # verbose_name = 'alwaleed' to change the table name

class Video(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
    # to change the ovjects name to it is real name
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=50)
    joined_date = models.DateField(verbose_name='Joined Date', default=timezone.now(), editable=False)
    Products = models.OneToOneField(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    # ForeignKey = Many to One
    Products = models.ForeignKey(Product, on_delete=models.CASCADE)
    watch = models.ManyToManyField(Video)

    def __str__(self):
        return self.name
    
