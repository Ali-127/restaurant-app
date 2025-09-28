from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout as django_logout
import random
import string
from restaurant.forms import AddForm, OrderForm
from .models import Menu, MenuItem, Order, OrderItem

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    next_url = request.POST.get('next') or request.GET.get('next') or 'home'
    # Handle login from submission
    if request.method == 'POST' and 'login' in request.POST:
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
            print(next_url)
            return redirect(next_url)
        messages.error(request, f'Invalid credentials.{form_login.errors}')
    
    # Handle register
    elif request.method == 'POST' and 'register' in request.POST:
        form_register = UserCreationForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            # login user afeter sign up
            login(request, user)
            return redirect(next_url)
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


def menu_page(request):
    # handle search field queries
    search_query = request.GET.get('search', '')
    if search_query:
        items = MenuItem.objects.filter(
            name__icontains=search_query,
            is_available=True
        )
    # Get all available items from database
    else:
        items = MenuItem.objects.filter(is_available=True)
        
    if request.method == "POST":
        item_id = request.POST.get('selected_item')
        
        # session cart
        cart = request.session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        request.session['cart'] = cart
    
    # Add to cart form
    add_form = AddForm() 
    
    return render(request, 'menu.html', {"items": items, "add_form": add_form, "search_query": search_query})

def cart_page(request):
    #  Handle increase and decrease buttons in cart page
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")
        cart = request.session.get('cart', {})
        
        if action == "increase":
            # get item from session
            cart[item_id] = cart.get(item_id, 0) + 1
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

@login_required
def place_order(request):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect('cart')
        
        total = 0
        order_items_data = []
        
        for item_id, quantity in cart.items():
            menu_item = MenuItem.objects.get(id=item_id)
            subtotal = menu_item.price * quantity
            total += subtotal
            
            order_items_data.append({
                'menu_item': menu_item,
                'quantity': quantity,
                'price': menu_item.price
            })
        
        #  Generate a random order-id for order
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        order = Order.objects.create(
            user=request.user,
            order_id=order_id,
            total_amount=total
        )
        
        # create order items using cart info
        for item_data in order_items_data:
            OrderItem.objects.create(
                order=order,
                menu_item=item_data['menu_item'],
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            
        # Clear cart
        request.session['cart'] = {}
        
        messages.success(request, f"Order placed successfully! Order ID: {order_id}")
        return render(request, 'congrats.html', {'order_id': order_id})
    
    return redirect('cart')


@login_required
def track_page(request):
    # Get user's orders newest first
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    order_details = []
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_details.append({
            'order': order,
            'items': items,
            'item_quantity': sum(item.quantity for item in items)
        })
    
    return render(request, 'track.html', {'order_details': order_details})


def table_page(request):
    return render(request, 'table.html')


def order_id_page(request):
    return render(request, 'order-id.html')

def otp_page(request):
    return render(request, 'otp.html')


def reservations_page(request):
    return render(request, 'table.html')

def delivery_page(request):
    return render(request, 'track.html')

def congrats_page(request):
    return render(request, 'congrats.html')
