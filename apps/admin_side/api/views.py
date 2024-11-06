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
    permission_classes = [AllowAny]  # Override later for superuser check

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if not user.is_superuser:
            return Response(
                {"detail": "Only admin users can log in here."},
                status=status.HTTP_403_FORBIDDEN
            )

        tokens = serializer.get_tokens(user)
        return Response({"email": user.email, "tokens": tokens}, status=status.HTTP_200_OK)
    


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
    

    














