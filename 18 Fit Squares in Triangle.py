for _ in range(int(input())):
	B = int(input()) #Base length
	'''
	  If B is even, then the maximum number of squares (n) there can be in one row 
	(|| to the base) is (B - 2) / 2. 
	  If B is odd, then n will be (B - 3) / 2.
	The total number of squares can be found out by summing up the first n 
	natural numbers using the progression formula (n * (n + 1)) / 2.
	'''
	n = (B - 2) // 2 if B % 2 == 0 else (B - 3) // 2
	squares = lambda n: (n * (n + 1)) // 2
	print(squares(n))
 
