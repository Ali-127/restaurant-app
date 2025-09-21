from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout, name="logout"),   
    path('forgot/', views.forgot_password_page, name="forgot"),   
]