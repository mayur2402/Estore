from django.contrib import admin
from .models import Category,Product,User,Order

# Register your models here.

class AdminProduct(admin.ModelAdmin):
	list_display = ['name','price','category']

class ProductCategory(admin.ModelAdmin):
	list_display = ['name']

class AdminUser(admin.ModelAdmin):
	list_display = ['fname','lname','email','phone']

class AdminOrder(admin.ModelAdmin):
	list_display = ['name','pname','price','date','city','address']

admin.site.register(Category,ProductCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(User,AdminUser)
admin.site.register(Order,AdminOrder)