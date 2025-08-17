from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import datetime
from .models import Reservation


# Create your tests here.
class ReservationTests(APITestCase):
    # Ensure we can create reservation object
    def test_create_reservation(self):
        url = reverse('reservation-list')
        reservation_date = datetime.date(2025, 8, 21)
        reservation_time = datetime.time(19, 00)
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'date': reservation_date,
            'time': reservation_time,
            'numbers_of_guests': 4,
            'special_requests': 'Near a window.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(Reservation.objects.get().name, 'John Doe')
    
    def test_list_reservations(self):
        # Ensure we can retrieve a list of reservations        
        Reservation.objects.create(
            name='Jane Smith',
            email='jane.smith@example.com',
            phone_number='1234567890',
            date='2025-08-21',
            time='20:30',
            numbers_of_guests=2,
        )
        url = reverse('reservation-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
