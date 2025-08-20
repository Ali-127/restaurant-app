from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout, name='logout'),
    path('reservations/', views.reservations_page, name='reservations'),
    path('delivery/', views.delivery_page, name='delivery'),
    path('cart/', views.cart_page, name='cart'),
    path('congrats/', views.congrats_page, name='congrats'),
    path('forgot-password/', views.forgot_password_page, name='forgot'),
    path('menu/', views.menu_page, name='menu'),
    path('order-id/', views.order_id_page, name='order_id'),
    path('otp/', views.otp_page, name='otp'),
    path('table/', views.table_page, name='table'),
    path('track/', views.track_page, name='track'),
]
