import math
fibo_series = [0, 1]

for _ in range(10**7):
    fibo_series.append((fibo_series[-1] + fibo_series[-2]) % 10)
    
for _ in range(int(input())):
	N = int(input())
	time = int(math.log2(N))
	i = 2**time - 1
	print(fibo_series[i])