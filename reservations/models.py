from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    numbers_of_guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
