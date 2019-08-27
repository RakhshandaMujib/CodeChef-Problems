T = int(input())

for _ in range(T):
	s = input()
	if s == s.lower() or s == ' ':
		if 'not' in list(s.split()):
			print('Real Fancy')
		else:
			print('regularly fancy')