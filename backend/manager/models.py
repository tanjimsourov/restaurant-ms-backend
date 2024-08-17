from accounts.restaurantModel import Restaurant
from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'material/{filename}'.format(filename=filename)


class rawMaterial(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='rawMaterial', on_delete=models.CASCADE)
    materialName = models.CharField(
        'Material',
        max_length=50,
        default='',
        null=False
    )
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='profilePic/default.jpg')
    inStock = models.FloatField(default=0)
    unitPrice = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)


class Purchase(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='Purchase', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Purchase', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='PurchaseItem', on_delete=models.CASCADE)
    material = models.ForeignKey(rawMaterial, related_name='materialID', on_delete=models.CASCADE)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Use(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='Use', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Use', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class UseItem(models.Model):
    useId = models.ForeignKey(Use, related_name='UseItem', on_delete=models.CASCADE)
    material = models.ForeignKey(rawMaterial, related_name='UseItem', on_delete=models.CASCADE)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

