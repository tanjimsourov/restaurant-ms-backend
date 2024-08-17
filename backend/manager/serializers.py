from rest_framework import serializers
from .models import rawMaterial, UseItem, Purchase, PurchaseItem


class AddMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = rawMaterial
        fields = ('materialName', 'image', 'inStock', 'unit_price')


class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseItem
        fields = (
            "material",
            "quantity",
        )


class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = (
            "id",
            "items",
            "total"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase = Purchase.objects.create(**validated_data)
        for item_data in items_data:
            PurchaseItem.objects.create(purchase=purchase, **item_data)
            item = rawMaterial.objects.get(materialName=item_data["material"])
            item.inStock = item.inStock + item_data["quantity"]
            item.save()

