for _ in range(int(input())):
	x_a, x_b, X_a, X_b= map(int, input().split())
	print(int((X_a / x_a) + (X_b / x_b)))
