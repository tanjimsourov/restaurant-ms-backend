from rest_framework import serializers
from .models import foodItem, Order, OrderItem


class AddFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodItem
        fields = '__all__'


class FoodItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodItem
        fields = 'isAvailable'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "item",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "restaurant",
            "items",
            "user",
            "total"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = validated_data.pop('total')
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            item = foodItem.objects.get(name=item_data["item"])
            order.total += item.unitPrice * item_data["quantity"]
        order.total = total
        return order
