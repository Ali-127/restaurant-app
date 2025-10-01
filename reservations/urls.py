from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.reservations_page, name="table"),
    path('reserve_slot/', views.reserve_slot, name="reserve"),
    path('cancel/', views.cancel_reservation, name="cancel_reservation"),
]
