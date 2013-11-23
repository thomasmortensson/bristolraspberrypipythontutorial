''' Exercise 2 '''

''' improve calculator so it does addition '''

'''
num1 = int(raw_input("Enter first number: "))
operator = raw_input("Enter operator (e.g. +, -, *, /): ")
num2 = int(raw_input("Enter second number: "))
if operator == "+":
	result = num1 + num2
	print num1, '+', num2, '=', result
if operator == "-":
	result = num1 - num2
	print num1, '-', num2, '=', result
if operator == "*":
	result = num1 * num2
	print num1, '*', num2, '=', result
if operator == "/":
	result = num1 / num2
	print num1, '/', num2, '=', result
'''

'''Extension'''

'''
num1 = float(raw_input("Enter first number: "))
operator = raw_input("Enter operator (e.g. +, -, *, /): ")
num2 = float(raw_input("Enter second number: "))
if operator == "+":
	result = num1 + num2
	print num1, '+', num2, '=', result
if operator == "-":
	result = num1 - num2
	print num1, '-', num2, '=', result
if operator == "*":
	result = num1 * num2
	print num1, '*', num2, '=', result
if operator == "/":
	result = num1 / num2
	print num1, '/', num2, '=', result
'''

''' print 0-100 ***inclusive*** '''

#for i in xrange(0,101):
#	print i

''' find 2 different ways to print 30 - 50 using different xranges'''

'''Sol1'''
#for i in xrange(30,51):
#	print i

'''Sol2'''
#for i in xrange(0,100):
#	if i >= 30 and i <= 50:
#		print i

'''print all numbers between 20-25 and 70-80 using a single loop'''
#for i in xrange(0,100):
#	if i >= 20 and i <= 25:
#		print i
#	if i >= 70 and i <= 80:
#		print i

'''print all numbers between 0-80 that are divisible by 4'''
'''
for i in xrange(0, 81):
	if i % 4 == 0:
		print i
'''

'''print all numbers between 0-80 that are divisible by 4 that aren't between 10 and 25'''
for i in xrange(0, 81):
	if i % 4 == 0:
		if i < 10 or i > 25:
			print i






