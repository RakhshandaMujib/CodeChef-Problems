T = int(input())
sums = [0 for i in range(T)]
for i in range(T):
    num = int(input())
    while num > 0:
    	num, sums[i] = (num // 10), (sums[i] + (num % 10))
for i in sums:
	print(i)    
    