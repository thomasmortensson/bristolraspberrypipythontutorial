''' Exercise 3 '''

''' Use Functions in calculator '''

def add(num1, num2):
	result = num1 + num2
	print num1, '+', num2, '=', result

def subtract(num1, num2):
	result = num1 - num2
	print num1, '-', num2, '=', result

def multiply(num1, num2):
	result = num1 * num2
	print num1, '*', num2, '=', result

def divide(num1, num2):
	result = num1 / num2
	print num1, '/', num2, '=', result

num1 = int(raw_input("Enter first number: "))
operator = raw_input("Enter operator (e.g. +, -, *, /): ")
num2 = int(raw_input("Enter second number: "))
if operator == "+":
	add(num1, num2)
if operator == "-":
	subtract(num1, num2)
if operator == "*":
	multiply(num1, num2)
if operator == "/":
	divide(num1, num2)