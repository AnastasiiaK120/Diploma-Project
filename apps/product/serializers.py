from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'category', 'vendor', 'title', 'slug', 'description', 'price', 'date_added', 'image', 'thumbnail')
        model = Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()

