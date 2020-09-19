#user entered version

product = str(input('what is the product url?'))
urname = str(input('your name?'))
email = input('your email?')
phone = input('your phone #?')
address = input('street address?')
zipf = input('zip code?')
cardn = input('credit card number?')
ccv = input('ccv?')
month = input('expiration month?')
exyear = input('expiration year?')


info = {}


info['product'] = product
info['name'] = urname
info['email'] = email
info['phone'] = phone
info['address'] = address
info['zip'] = zipf
info['cardn'] = cardn
info['ccv'] = ccv
info['month'] = month
info['exyear'] = exyear


print(info)





keys = {"products": info['product'],
       	"name": info['name'],
	"email": info['email'],
	"phone": info['phone'],
	"address": info['address'],
	"zip": info['zip'],
	"cardn": info['cardn'],
	"ccv": info['ccv'],
	"month": info['month'],
	"year": info['exyear'] }



print(keys)
