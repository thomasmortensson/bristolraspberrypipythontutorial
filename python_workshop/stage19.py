''' FUNCTIONS 2 '''

def add_numbers(num1, num2):
	result = num1 + num2
	return result

result = add_numbers(1, 2)
print result

result = 0
for i in xrange(0, 10):
	new_result = add_numbers(result, i)
	print result, "+", i, "=", new_result
	result = new_result