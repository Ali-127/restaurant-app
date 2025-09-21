from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
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

def forgot_password_page(request):
    return render(request, 'forgot.html')
