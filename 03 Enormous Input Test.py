(n, k) = map(int, input().split(' '))
count = 0
for i in range(n):
	num = int(input())
	if num % k == 0:
		count += 1
print(count)	