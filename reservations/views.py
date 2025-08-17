from django.shortcuts import render
from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer

# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
