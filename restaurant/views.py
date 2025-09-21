from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Menu, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    """Handle login form display and submission."""
    if request.method == 'POST':
        form_login = AuthenticationForm(request=request, data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
            return redirect('home')
        
    form_login = AuthenticationForm()
    form_register = UserCreationForm()
    return render(request, "login.html", {"form_login": form_login, "form_register": form_register})


def register_page(request):
    """Handle registration form display and submission."""
    if request.method == "POST":
        form_register = UserCreationForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            login(request, user)
            return redirect('home')
    form_register = UserCreationForm()
    form_login = AuthenticationForm()
    
    return render(request, "login.html", {"form_login": form_login, "form_register": form_register})
    
    
def logout(request):
    logout(request=request)
    return redirect('home')

def reservations_page(request):
    return render(request, 'table.html')

def delivery_page(request):
    return render(request, 'track.html')

def cart_page(request):
    return render(request, 'cart.html')

def congrats_page(request):
    return render(request, 'congrats.html')

def forgot_password_page(request):
    return render(request, 'forgot.html')

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
    
