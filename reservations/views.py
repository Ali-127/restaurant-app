from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


def reservation_page(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation created successfully!')
            return redirect('congrats')
        else:
            form = ReservationForm
            
        return render(request, 'table.html', {'form': form})
    