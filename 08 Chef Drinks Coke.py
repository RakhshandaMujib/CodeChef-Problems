T = int(input())
for _ in range(T): #Iterating through all the test cases.
	N, M, K, L, R = map(int, input().split())
	max_P, result = 1000000, -1
	for _ in range(N): #For each can in a test case...
		C, P = map(int, input().split())
		for _ in range(M): #For each minute in M if C of can is...
			if C < K - 1:
				C += 1
			elif C > K + 1:
				C -= 1
			elif (K - 1 <= C) and (C <= K + 1):
				C = K
		if (L <= C) and (C <= R):
			if P <= max_P:
				max_P, result = P, P
	print(result)