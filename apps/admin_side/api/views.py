from django.shortcuts import render
from ..views_base import CustomModelViewset
from ..permissions import IsSuperUser
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from ..models import *
from .serializers import *

# Create your views here.

class AdminLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Sizeviewset(CustomModelViewset):
    permission_classes = [IsSuperUser]
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ProductViewset(CustomModelViewset):
    permission_classes = [IsSuperUser]
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductListSerializer
        return ProductSerializer
    

    














