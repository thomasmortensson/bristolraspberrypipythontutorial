''' <, <=, ==, >=, >'''

below_test = 5
above_test = 10
equals_test = 8

current_num = int(raw_input("Enter a number to test: "))

if current_num < below_test:
	print 1

if current_num > above_test:
	print 2

if current_num == equals_test:
	print 3

if current_num <= below_test:
	print 4

if current_num >= above_test:
	print 5

