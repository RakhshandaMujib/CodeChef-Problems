S = input()
N = int(input())
for _ in range(N):
	W = input()
	if set(W) <= set(S):
		print('Yes')
	else:
		print('No')
