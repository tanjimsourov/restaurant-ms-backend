from accounts.restaurantModel import User
from django.db import models


class rawMaterial(models.Model):
    restaurant = models.ForeignKey(User, related_name='restaurant', on_delete=models.CASCADE)
    marName = models.CharField(
        _('Material'),
        max_length=50,
        default='',
        null=False
    )
    bal = models.FloatField(default=0)
    unitPrice = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)


class Purchase(models.Model):
    restaurant = models.ForeignKey(User, related_name='restaurant', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class PurchaseItem(models.Model):
    bazar = models.ForeignKey(Purchase, related_name='bazarNo', on_delete=models.CASCADE)
    material = models.ForeignKey(rawMaterial, related_name='material', on_delete=models.CASCADE)
    quantity = models.FloatField()


class Use(models.Model):
    restaurant = models.ForeignKey(User, related_name='restaurant', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class UseItem(models.Model):
    bazar = models.ForeignKey(Purchase, related_name='bazarNo', on_delete=models.CASCADE)
    material = models.ForeignKey(rawMaterial, related_name='material', on_delete=models.CASCADE)
    quantity = models.FloatField()