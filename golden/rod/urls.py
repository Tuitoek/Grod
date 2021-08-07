from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    
    path('',views.store, name='store'),
    path('cart/', views.cart,name='cart'),
    path('checkout/',views.checkout,name='chechout'),
    url(r'^accounts/',include('registration.backends.simple.urls')),



]