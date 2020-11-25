from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category,User,Order
from django.contrib.auth.hashers import check_password,make_password
from store.templatetags import Cart
import datetime

error = {}
error['key'] = ''
user = None
otp1 = None

def products(request):
	#Get request
	if request.method == "GET":
		category = Category.get_all_category()
		product = None
		Cid = request.GET.get('cat')
		if Cid:
			product = Product.get_product_by_categoryid(Cid)
		else:
			product = Product.get_all_product()

		data = {}
		data['Product'] = product
		data['Category'] = category

		return render(request,'index.html',data)
	#Post Request
	else:
		product_id = request.POST.get('pid')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product_id)
			if quantity:
				if remove:
					if quantity == 1:
						cart.pop(product_id)
					else:
						cart[product_id] = quantity - 1
				else:
					cart[product_id] = quantity + 1
			else:
				cart[product_id] = 1
		else:
			cart = {}
			cart[product_id] = 1

		request.session['cart'] = cart
		return redirect('product')

def signup(request):
	if request.method == 'GET':
		return render(request,'SignUp.html')

	else:
		fname = request.POST.get('Fname')
		lname = request.POST.get('Lname')
		email = request.POST.get('Email')
		phone = request.POST.get('Phone')
		password = request.POST.get('Password1')
		passwordagain = request.POST.get('Password2')

		if not password == passwordagain:
			error['key'] = 'Password and re enter password must be same'
			return render(request,'SignUp.html',error)
		elif not len(phone) == 10:
			error['key'] = 'Phone number should be 10 number'
			return render(request,'SignUp.html',error)
		elif User.checkemail(email):
			error['key'] = 'User already exits'
			return render(request,'SignUp.html',error)
		else:
			password = make_password(password)
			passwordagain = make_password(passwordagain)
			global otp1,user
			otp1 = User.send_Email(email)
			user = User(fname=fname,lname=lname,email=email,phone=phone,password=password,passwordagain=passwordagain)
			return render(request,"confirmation.html")

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		email = request.POST.get('email')
		password = request.POST.get('password')
		userobj = User.get_user_by_email(email)
		name = userobj.fname
		print(name)
		if userobj:
			if check_password(password,userobj.password):
				request.session['userobj_id']=userobj.id
				request.session['uname'] = name
				return redirect('product')
			else:
				error['key'] = 'Incorrect email or password'
				return render(request,'login.html',error)
		else:
			error['key'] = 'Incorrect email or password'
			return render(request,'login.html',error)

def logout(request):
	request.session.clear()
	return redirect('product')

def confirm(request):
	otp2 = request.POST.get('otp')

	if otp1 == otp2:
		user.register()
		return redirect('product')
	else:
		return redirect("SignUp")

def cart(request):
	if request.session.get('cart'):
		idlist = list(request.session.get('cart').keys())
		Productlist = Product.get_product_by_id(idlist)
		return render(request,'Cart.html',{'products' : Productlist})
	else:
		return render(request,'Cart.html')

def placeorder(request):
	return render(request,'Orders.html')
	
def order(request):
	if request.method == "POST":
		user = User.get_user_by_id(request.session.get('userobj_id'))
		name = user.fname
		cart = request.session.get('cart')
		products = Product.get_product_by_id(list(cart.keys()))
		for product in products:
			if user:
				pname = product.name
				request.session['name'] = name
				date = request.POST.get('date')
				anothernumber = request.POST.get('anothernumber')
				city = request.POST.get('city')
				address = request.POST.get('address')
				quantity = Cart.times_quantity(product,cart)
				status = request.POST.get('status')
				
				order = Order(user = User(id = user.id),name = name,pname = pname,product = product,quantity = quantity,price = Cart.Total(product,cart),anothernumber = anothernumber,city = city,address = address,status = status)
				order.register()
		return redirect('product')

	return redirect('login')

def vieworder(request):
	data = Order.get_detail()
	return render(request,'vieworder.html',{'data':data})

