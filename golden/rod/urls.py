from django.urls import path

from . import views



urlpatterns = [
<<<<<<< HEAD
    
    path('',views.store, name='store'),
    path('cart/', views.cart,name='cart'),
    path('checkout/',views.checkout,name='chechout'),
    path('about/',views.about,name="about"),
    path('register/',views.register, name = "register"),
    path('login',views.login,name="login"),
    path("logout",views.logout_request,name="logout"),

=======
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
>>>>>>> 0b088f20cc06084d783b4f1f097786b51eda73eb

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]