for _ in range(int(input())):
	top, bot = input(), input()
	flag = False
	for i in range(3):
		if top[i] == 'o' or bot[i] == 'o':
			b_count = 0
			for j in range(3):
				if i != j and (top[j] == 'b' or bot[j] == 'b'):
					b_count += 1
			if b_count == 2:
				flag = True
	if flag:
		print('yes')
	else: 
		print('no')