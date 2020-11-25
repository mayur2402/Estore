from django.db import models
import random,datetime,string
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password

class Category(models.Model):
	name = models.CharField(max_length = 15)

	def __str__(self):
		return self.name

	@staticmethod
	def get_all_category():
		return Category.objects.all()


class Product(models.Model):
	name = models.CharField(max_length = 30)
	price = models.IntegerField(default = 0)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	description = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'upload/img')

	@staticmethod
	def get_all_product():
		return Product.objects.all()

	@staticmethod
	def get_product_by_id(ids):
		return Product.objects.filter(id__in = ids)

	@staticmethod
	def get_product_byid(id):
		return Product.objects.filter(id = id)

	@staticmethod
	def get_product_by_categoryid(id):
		return Product.objects.filter(category = id)

class User(models.Model):
	fname = models.CharField(max_length = 50)
	lname = models.CharField(max_length = 50)
	email = models.EmailField()
	phone = models.IntegerField()
	password = models.CharField(max_length = 300)
	passwordagain = models.CharField(max_length = 300)

	def register(self):
		self.save()

	@staticmethod
	def get_user_by_id(id):
		return User.objects.get(id = id) 
	
	@staticmethod
	def get_user_by_email(email):
		try:
			return User.objects.get(email = email)
		except:
			return False

	def checkemail(email):
		return User.objects.filter(email = email)

	def send_Email(email):
		digit = string.digits
		otp = ''.join(random.choices(string.digits, k = 5))
		subject = "User Authentication"
		message = "One time generated password is "+otp
		from_email = "email@gmail.com"
		to_email = email
		send_mail(subject,message,from_email,[to_email],fail_silently=False,)

		return otp

class Order(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	name = models.CharField(max_length = 50,default = ' ')
	pname = models.CharField(max_length = 50,default = ' ')
	product = models.CharField(max_length = 200)
	quantity = models.IntegerField()
	price = models.IntegerField()
	date = models.DateField(default = datetime.datetime.today)
	anothernumber = models.IntegerField(default = 0)
	city = models.CharField(max_length = 20,default = 'pune')
	address = models.CharField(max_length = 200,default = '')
	status = models.BooleanField(default = 'False')

	def register(self):
		self.save()

	@staticmethod
	def get_detail():
		return Order.objects.all()

	@staticmethod
	def get_order_by_customer(customer_id):
		return Order.objects.filter(user = customer_id)