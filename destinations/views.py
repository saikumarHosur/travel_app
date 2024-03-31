from rest_framework import generics
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Destination
from .serializers import DestinationSerializer

class CustomExceptionHandlerMixin:
    
    # handling exceptions in API views
    def handle_exception(self, exc):
        
        #returns responses.
        if isinstance(exc, ValidationError):
            return Response({"error": "Invalid data", "details": exc.detail}, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exc, NotFound):
            return Response({"error": "Destination not found"}, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exc, PermissionDenied):
            return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exc, ObjectDoesNotExist):
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

class DestinationListCreateAPIView(generics.ListCreateAPIView, CustomExceptionHandlerMixin):
   
    # API view for listing and creating data in data base.
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class DestinationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CustomExceptionHandlerMixin):
    
    # API view for retrieving, updating, and deleting a destination.
    
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
