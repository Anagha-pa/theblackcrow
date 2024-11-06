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
                raise serializers.ValidationError(_('Invalid email or password.'))
            if not user.is_superuser:
                raise serializers.ValidationError(_('User is not an admin.'))
        else:
            raise serializers.ValidationError(_('Must include "email" and "password".'))

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }



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
        

        

