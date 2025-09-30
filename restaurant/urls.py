from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_page, name='cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('menu/', views.menu_page, name='menu'),
    path('track/', views.track_page, name='track'),
]
