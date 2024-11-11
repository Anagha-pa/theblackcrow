from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from ..models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "username", "password", "mobile"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'], mobile=validated_data['mobile'])
        user.set_password(validated_data['password'])
        user.save()
        return user


