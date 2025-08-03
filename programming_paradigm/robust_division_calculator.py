def safe_divide(numerator, denominator):
	try:
		num1 = float(numerator)
		num2 = float(denominator)
		return num1 / num2
	except ZeroDivisionError:
		return "Can not divide by zero"
	except ValueError:
		return "Input should be a number"