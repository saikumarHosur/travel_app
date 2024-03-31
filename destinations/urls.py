from django.urls import path
from .views import DestinationListCreateAPIView, DestinationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('destinations/', DestinationListCreateAPIView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDestroyAPIView.as_view(), name='destination-detail'),
]

