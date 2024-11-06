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
            # Authenticate the user
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Create JWT token for the authenticated user
                refresh = RefreshToken.for_user(user)
                # Return email and the JWT token
                return Response(
                    {'email': user.email, 'token': str(refresh.access_token)},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'detail': 'Invalid credentials.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
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
    

    














