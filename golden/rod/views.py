from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product, Category,Shop,User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def store(request):
    context = {}
    return render (request,'store/store.html')
    
def cart(request):
    context = {}
    return render (request,'store/cart.html') 

def checkout(request):
    context = {}
    return render (request,'store/checkout.html') 

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
    return render(request,"registration/login.html",{"form":form})

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

    