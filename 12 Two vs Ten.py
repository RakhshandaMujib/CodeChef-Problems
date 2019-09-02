for _ in range(int(input())):
	x = int(input())
	turn = 0 if x % 10 == 0 else (1 if x % 10 == 5 else -1)
	print(turn)