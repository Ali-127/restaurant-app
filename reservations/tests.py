from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, time
from .models import Reservation


class ReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password='12345')
        
    def test_reservation_creation(self):
        reservation = Reservation.objects.create(
            user=self.user,
            date=date(2025, 12, 25),
            time=time(19, 0),
        )
        
        self.assertEqual(reservation.user, self.user)

