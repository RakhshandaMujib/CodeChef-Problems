for _ in range(int(input())):
	D, d, P, Q= map(int, input().split())
	n = D // d
	r = D % d
	sum_is = n * (n - 1) / 2
	n_intervals = d * ((n * P) + (sum_is * Q))
	remainder = r * (P + n * Q)
	ans = n_intervals + remainder
	print(int(ans))
