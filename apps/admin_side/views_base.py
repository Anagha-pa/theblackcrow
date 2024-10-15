from rest_framework.response import Response
from rest_framework import status, viewsets

class CustomModelViewset(viewsets.ModelViewSet):
    # base class for handling common crud operation with custom response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'success':True,
            'message':'Data posted',
            'data':serializer.data
        }, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'success':True,
            'message':'Data updated',
            'data':serializer.data
        })
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success':True,
            'message':'Data destroyed',
            
        })
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success':True,
            'message':'Data retrieved',
            'data':serializer.data
        })
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'message': 'Data retrieved',
            'data': serializer.data
        })
    
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        return Response({
            "success": False,
            "message": str(exc),
            "data": None
        }, status=response.status_code)

