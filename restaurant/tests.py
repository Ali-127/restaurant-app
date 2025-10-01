from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem, Menu


class CartTestCase(TestCase):
    def setUp(self):
        # Create test client
        self.client = Client()
        
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        # Create test menu and items
        self.menu = Menu.objects.create(name="Test Menu")
        self.item1 = MenuItem.objects.create(
            menu=self.menu,
            name="Burger",
            price=10.99,
            is_available=True
        )
        self.item2 = MenuItem.objects.create(
            menu=self.menu,
            name="Pizza",
            price=15.99,
            is_available=True
        )
    
    def test_add_item_to_cart(self):
        """Test adding a single item to cart"""
        response = self.client.post(reverse('menu'), {
            'selected_item': self.item1.id
        })
        
        # Check if item was added to session
        session = self.client.session
        cart = session.get('cart', {})
        
        self.assertIn(str(self.item1.id), cart)
        self.assertEqual(cart[str(self.item1.id)], 1)
    
    def test_add_multiple_same_items(self):
        """Test adding same item multiple times increases quantity"""
        # Add item first time
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        # Add same item again
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        session = self.client.session
        cart = session.get('cart', {})
        
        # Should have quantity of 2
        self.assertEqual(cart[str(self.item1.id)], 2)
    
    def test_add_different_items(self):
        """Test adding different items to cart"""
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        self.client.post(reverse('menu'), {'selected_item': self.item2.id})
        
        session = self.client.session
        cart = session.get('cart', {})
        
        # Should have 2 different items
        self.assertEqual(len(cart), 2)
        self.assertIn(str(self.item1.id), cart)
        self.assertIn(str(self.item2.id), cart)
    
    def test_cart_persists_across_pages(self):
        """Test cart persists when navigating to cart page"""
        # Add item to cart
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        # Navigate to cart page
        response = self.client.get(reverse('cart'))
        
        # Check cart still has item
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Burger')
    
    def test_increase_cart_quantity(self):
        """Test increasing item quantity in cart"""
        # Add item to cart first
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        # Increase quantity
        self.client.post(reverse('cart'), {
            'item_id': self.item1.id,
            'action': 'increase'
        })
        
        session = self.client.session
        cart = session.get('cart', {})
        
        self.assertEqual(cart[str(self.item1.id)], 2)
    
    def test_decrease_cart_quantity(self):
        """Test decreasing item quantity in cart"""
        # Add item twice
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        # Decrease quantity
        self.client.post(reverse('cart'), {
            'item_id': self.item1.id,
            'action': 'decrease'
        })
        
        session = self.client.session
        cart = session.get('cart', {})
        
        self.assertEqual(cart[str(self.item1.id)], 1)
    
    def test_remove_item_from_cart(self):
        """Test removing item completely from cart"""
        # Add item
        self.client.post(reverse('menu'), {'selected_item': self.item1.id})
        
        # Remove item
        self.client.post(reverse('cart'), {
            'item_id': self.item1.id,
            'action': 'remove'
        })
        
        session = self.client.session
        cart = session.get('cart', {})
        
        self.assertNotIn(str(self.item1.id), cart)
    
    def test_empty_cart_displays_message(self):
        """Test empty cart shows appropriate message"""
        response = self.client.get(reverse('cart'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'empty')
        