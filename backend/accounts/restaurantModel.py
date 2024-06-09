import datetime
from datetime import date
from django.db import models


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100, default='')
    restaurant_address = models.CharField(max_length=100, default='')
    restaurant_description = models.CharField(max_length=1024, default='')
    staff_count = models.IntegerField(default=0)
    manager_count = models.IntegerField(default=0)
    waiter_count = models.IntegerField(default=0)
    admin_count = models.IntegerField(default=0)
    totalEarn = models.FloatField(default=0)
    totalCost = models.FloatField(default=0)
    Monthly_earn = models.FloatField(default=0)
    Monthly_cost = models.FloatField(default=0)
    Yearly_earn = models.FloatField(default=0)
    Yearly_cost = models.FloatField(default=0)
    Most_selling_item = models.CharField(max_length=100, default='')
    Monthly_profit = models.FloatField(default=0)
    Yearly_profit = models.FloatField(default=0)
    DayUsed = models.FloatField(default=0)
    openingDate = models.DateField(auto_now_add=True)
    closingDate = models.DateField(null=True)
