from django.urls import path 
from . import views

urlpatterns = [
path('',views.register,name='register'),
path('login/',views.LoginPage,name='login'),
path('logout/',views.LogoutPage,name='logout'),

  path("home/", views.home, name="home"),

  
  
]  