from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout as django_logout
from .models import Menu, MenuItem

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def reservations_page(request):
    return render(request, 'table.html')

def delivery_page(request):
    return render(request, 'track.html')

def cart_page(request):
    return render(request, 'cart.html')

def congrats_page(request):
    return render(request, 'congrats.html')

def menu_page(request):
    return render(request, 'menu.html')

def order_id_page(request):
    return render(request, 'order-id.html')

def otp_page(request):
    return render(request, 'otp.html')

def table_page(request):
    return render(request, 'table.html')

def track_page(request):
    return render(request, 'track.html')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserCreationForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    django_logout(request)
    return redirect('home')
