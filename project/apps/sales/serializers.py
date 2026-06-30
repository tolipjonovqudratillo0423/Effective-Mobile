from rest_framework import serializers

from apps.sales.models import (
    Order,
    Product
)

#======================================================================
# Product Serializer
#======================================================================

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            "name",
            "price"
        ]



#======================================================================
# Order Serializer
#======================================================================

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    
    class Meta:
        model = Order
        fields = [
            "product",
            "quantity",
            "total",
        ]



