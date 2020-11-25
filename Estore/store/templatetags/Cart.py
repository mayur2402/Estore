from django import template

register = template.Library()

total = 0
@register.filter(name = 'is_in_cart')
def is_in_cart(product,cart):
	key = cart.keys()
	for kid in key:
		if kid.isdigit():
			if int(kid) == product.id:
				return True

	return False

@register.filter(name = 'times_quantity')
def times_quantity(product,cart):
	key = cart.keys()
	for kid in key:
		if kid.isdigit():
			if int(kid) == product.id:
				return cart.get(kid)
	return 0

@register.filter(name = 'Total')
def Total(product,cart):
	quantity = times_quantity(product,cart)
	product_total = quantity * product.price
	return product_total

@register.filter(name = 'total_price')
def total_price(products,cart):
	total = 0
	for product in products:
		P_total = Total(product,cart)
		total = total + P_total

	return total

@register.filter(name = 'Count')
def Count(cart):
	count = 0
	if cart:
		key = cart.keys()
		for i in key:
			count = count+1

	return count

@register.filter(name = 'orderprice')
def orderprice(data):
	price = 0
	for order in data:
		price = price + order.price

	return price

