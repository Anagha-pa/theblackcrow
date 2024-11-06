from rest_framework import serializers
from ..models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _



class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            data['user'] = user
        else:
            raise serializers.ValidationError('Email and password are required.')

        return data



class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    Product_size = serializers.SerializerMethodField

    class Meta:
        model = Product
        fields = '__all__'

    def get_Product_size(self, obj):
        if obj.Product_size:
            return {"id":obj.Product_size.id, "name":obj.Product_size.Product_size}
        

        

