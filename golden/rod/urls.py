from django.urls import path,include
from . import views
from django.conf.urls import url



urlpatterns = [
    
    path('',views.store, name='store'),
    path('cart/', views.cart,name='cart'),
    path('checkout/',views.checkout,name='chechout'),
    path('about/',views.about,name="about"),
    path('register/',views.register, name = "register"),
    path('login',views.login,name="login"),
    path("logout",views.logout_request,name="logout"),



]