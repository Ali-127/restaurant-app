from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import time, datetime
from .models import Reservation
from .forms import ReservationForm


def reservations_page(request):        
    time_slots = [
        time(11, 0),
        time(12, 0),
        time(13, 0),
        time(14, 0),
        time(18, 0),
        time(19, 0),
        time(20, 0),
        time(21, 0),
    ]
    
    # Use today's date
    current_date = datetime.now().date()
    
    reservations = Reservation.objects.filter(date=current_date)
    reserved_times = set(reservations.values_list('time', flat=True))

    # Check which slots belong to current user
    user_reservations = set()
    if request.user.is_authenticated:
        user_reservations = set(
            reservations.filter(user=request.user).values_list('time', flat=True)
        )
    
    # Build slots data
    slots = []
    for slot_time, table in zip(time_slots, range(1, len(time_slots) + 1)):
        slots.append({
            'table': table,
            'time': slot_time,
            'date': current_date,
            'is_reserved': slot_time in reserved_times,
            'is_user_reservation': slot_time in user_reservations,
            'accommodation': 4
        })
    reserve_form = ReservationForm()
    
    return render(request, 'table.html', {
        'slots': slots,
        'current_date': current_date,
        'reserve_form': reserve_form
        })

@login_required
def reserve_slot(request):
    if request.method == "POST":
        # Get time and date from post request
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        
        try:
            # Format time and date
            reservation_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            reservation_time = datetime.strptime(time_str, '%H:%M').time()
            
            # Show error if reservation exists
            if Reservation.objects.filter(date=reservation_date, time=reservation_time).exists():
                messages.error(request, "This slot is already reserved.")
            # Create reservation
            else:
                Reservation.objects.create(
                    user=request.user,
                    date=reservation_date,
                    time=reservation_time
                )
                messages.success(request, "Reservation successful!")
                
        except Exception as e:
            messages.error(request, f"Reservation failed. {e}")
            
    return redirect('table')
