from django.shortcuts import render, redirect
from django.contrib import messages
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
    # Handle login from submission
    if request.method == 'POST' and 'login' in request.POST:
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
            return redirect('home')
        messages.error(request, f'Invalid credentials.{form_login.errors}')
    
    # Handle register
    elif request.method == 'POST' and 'register' in request.POST:
        form_register = UserCreationForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            # login user afeter sign up
            login(request, user)
            return redirect('home')
        messages.error(request, f'Registration Failed.{form_register.errors}')
        print(f"error: {form_register.errors}")
        
    form_login = AuthenticationForm()
    # override default login form widget attributes
    form_login.fields['username'].widget.attrs.update({'placeholder': 'Username'})
    form_login.fields['password'].widget.attrs.update({'placeholder': 'Password'})
    
    form_register = UserCreationForm()
    # override default register form widget attributes
    form_register.fields['username'].widget.attrs.update({'placeholder': 'Username'})
    form_register.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
    form_register.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
    
    return render(request, 'login.html',
                  {'form_login': form_login,
                   'form_register': form_register,
                   })

def logout_view(request):
    django_logout(request)
    return redirect('home')
