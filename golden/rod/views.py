<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product, Category,Shop,User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
=======
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
>>>>>>> 0b088f20cc06084d783b4f1f097786b51eda73eb

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

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
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

<<<<<<< HEAD
def about(request):
    return render(request,'company/main.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('store')
        else:
            form = UserCreationForm()
    return render(request,'registration/registration.html',{'form':form})

def login(request):
    return render(request,"registration/login.html")

def logout_request(request):
    logout(request)
    messages.info(request,"logged out successfully!")
    return redirect("store")   

# def searchresults(request):
#     product_category = Category.objects.all()
#     shop = Shop.object.all()
#     product =Product.object.all
#     if 'users' in request.GET.get('users'):
#         searched_item = request.GET.get("users")
#         searched_category = category.search_by_category(search_term)
#         message = f"{search_term}"
#         return render(request, 'search.html', {"message": message, "users": searched_users})
#     else:
#         message = "You haven't searched for any term"
#     return render(request,'search.html', {"message": message,"images_item":images_item})

    
=======
	return JsonResponse('Payment submitted..', safe=False)
>>>>>>> 0b088f20cc06084d783b4f1f097786b51eda73eb
