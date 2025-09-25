from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
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


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
