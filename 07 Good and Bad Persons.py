T = int(input())

for case in range(T):
	N, k = map(int, input().split())
	s = input()
	up = low = 0

	for i in s:
		if i.islower():
			low += 1
		else:
			up += 1

	if low <= k and up > k:
		print('brother')
	elif low > k and up <= k:
		print('chef')
	elif low <= k and up <= k:
		print('both')
	else:
		print('none')