from rest_framework import serializers
from .models import Product, Order, OrderItem, ShippingAddress, Review
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'