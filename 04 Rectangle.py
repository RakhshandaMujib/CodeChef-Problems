T = int(input())
for i in range(T):
	l = list(map(int, input().split()))[:4] #Reading the list. 
	d = {i:0 for i in set(l)} #Creating a dictionary with unique length as key.
	for j in l:
		if j in d.keys():
			d[j] += 1 #If element is in dictionary, increment its value.
	value = set(d.values()) #Should be 2 if length and breadth are different.
							#Should be 4 if length and breadth aren't different.
	if value == {2} or value == {4}: 
		print('YES')
	else:
		print('NO')

#Much simpler way to approach this problem:
#T = int(input())
#for i in range(T):
#	l = list(map(int, input().split()))[:4]
#	l.sort()
#	if l[0] == l[1] and l[2] == l[3]:
#		print('YES')
#	else:
#		print('NO')