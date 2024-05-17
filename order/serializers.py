# serializers.py
from rest_framework import serializers
from .models import Order, Product
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    products = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all(), many=True)
    product_quantities = serializers.JSONField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'product_quantities', 'payment_info', 'created_at']

    def create(self, validated_data):
        products = validated_data.pop('products')
        product_quantities = validated_data.pop('product_quantities')
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        order.product_quantities = product_quantities
        order.save()
        return order

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)
        product_quantities = validated_data.pop('product_quantities', None)
        
        instance.user = validated_data.get('user', instance.user)
        instance.payment_info = validated_data.get('payment_info', instance.payment_info)
        
        if products is not None:
            instance.products.set(products)
        
        if product_quantities is not None:
            instance.product_quantities = product_quantities
        
        instance.save()
        return instance
