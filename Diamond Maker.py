while True:
	try:
		n = int(input("n: "))
		if n % 2 == 0: n -= 1
		for x in range(n):
			a = int(n - abs((2 * x) - (n - 1)))
			b = int((n - a) / 2)
			print(b * " " + a * "#" + b * " ")
	except:
		print("Input a number please!")