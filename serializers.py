# store/serializers.py

from rest_framework import serializers
from .models import Vegetable, VegetableRecipe, Order, Customer

class VegetableRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VegetableRecipe
        fields = ['id', 'recipe_name', 'instructions']

class VegetableSerializer(serializers.ModelSerializer):
    recipes = VegetableRecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Vegetable
        fields = ['id', 'name', 'price', 'image', 'recipes']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    vegetables = VegetableSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'vegetables', 'total_cost', 'order_date']
