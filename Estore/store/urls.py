from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path('',views.products,name = "product"),
	path('SignUp/',views.signup,name = "SignUp"),
	path('login/',views.login,name = 'login'),
	path('logout/',views.logout),
	path('confirm/',views.confirm),
	path('cart/',views.cart,name = "carts"),
	path('placeorder/',views.placeorder),
	path('order/',views.order),
	path('vieworder/',views.vieworder)
]
