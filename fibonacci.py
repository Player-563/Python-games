number1 = 0
number2 = 1
number3 = 0
repeat1 = 0
repeat2 = int(input("How many Fibonacci numbers: "))
while repeat1 != repeat2:
	number3 = number1 + number2
	print(number3)
	number1 = number2
	number2 = number3
	repeat1 = repeat1 + 1