from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    money = models.DecimalField(decimal_places=2, max_digits=10)


class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(blank=True, null=True)
    available_amount = models.IntegerField(null=True, blank=True)


class Purchase(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    purchase_time = models.TimeField(auto_now=True)


class Chargeback(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    chargeback_time = models.TimeField(auto_now=True)