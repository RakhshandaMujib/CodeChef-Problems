for _ in range(int(input())):
	N = int(input())
	v_i = sorted(list(map(int, input().split())))
	diff = sorted([v_i[x + 1] - v_i[x] for x in range(len(v_i) - 1)])
	print(diff[0])