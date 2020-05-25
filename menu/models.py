from django.db import models
from django.contrib.auth.models import User


class Breakfast(models.Model):
    item = models.CharField(max_length=30)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item


class Lunch(models.Model):
    item = models.CharField(max_length=30)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item


class Dinner(models.Model):
    item = models.CharField(max_length=30)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item


class Special(models.Model):
    item = models.CharField(max_length=30)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item

class Order(models.Model):
    item = models.CharField(max_length=30)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)
    qty = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
