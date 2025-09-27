from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout as django_logout

from restaurant.forms import AddForm, OrderForm
from .models import Menu, MenuItem

# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def menu_page(request):
    if request.method == "POST":
        item_id = request.POST.get('selected_item')
        
        # session cart
        cart = request.session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        request.session['cart'] = cart
        print(cart)
    # Get all available items from database
    items = MenuItem.objects.filter(is_available=True)
    
    # Add to cart form
    add_form = AddForm() 
    
    return render(request, 'menu.html', {"items": items, "add_form": add_form})

def cart_page(request):
    #  Handle increase and decrease buttons in cart page
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")
        cart = request.session.get('cart', {})
        
        if action == "increase":
            # get item from session
            cart[item_id] = cart.get(item_id, 0) + 1
            print(cart)
        elif action == "decrease":
            if item_id in cart:
                cart[item_id] -= 1
                # if quantity hits zero, delete item from cart
                if cart[item_id] <= 0:
                    del cart[item_id]
        elif action == "remove":
            if item_id in cart:
                del cart[item_id]
        
        #  update cart with new values
        request.session['cart'] = cart
        
    
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for item_id, quantity in cart.items():
        item = MenuItem.objects.get(id=item_id)
        subtotal = quantity * item.price
        total += subtotal
        
        cart_items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal
        })
    
    order_form = OrderForm
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'order_form': order_form
    })


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

def order_id_page(request):
    return render(request, 'order-id.html')

def otp_page(request):
    return render(request, 'otp.html')

def table_page(request):
    return render(request, 'table.html')

def track_page(request):
    return render(request, 'track.html')

def reservations_page(request):
    return render(request, 'table.html')

def delivery_page(request):
    return render(request, 'track.html')

def congrats_page(request):
    return render(request, 'congrats.html')
