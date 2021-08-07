from django.contrib import admin
from .models import Customer,Shop,Category,Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)

