from accounts.restaurantModel import Restaurant
from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'foods/{filename}'.format(filename=filename)


class foodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='foodItem', on_delete=models.CASCADE)
    foodItemName = models.CharField(
        'foodItem',
        max_length=50,
        default='',
        null=False
    )
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='foods/default.jpg')
    isAvailable = models.BooleanField(default=False)
    unitPrice = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='Order', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Order', on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    isDelivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='OrderItem', on_delete=models.CASCADE)
    item = models.ForeignKey(foodItem, related_name='foodItem', on_delete=models.CASCADE)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
