def flip(coins):
	for i in range(len(coins)):
		coins[i] = 'T' if coins[i] == 'H' else 'H'

for _ in range(int(input())):
	N, K = map(int, input().split())
	coins = list(input().split())
	for _ in range(K):
		if coins.pop() == 'H':
			flip(coins)
	print(coins.count('H'))