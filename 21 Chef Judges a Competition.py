for _ in range(int(input())): 
	N = int(input())
	A = sorted(list(map(int, input().split()))) #Sorting the input for Alice.
	B = sorted(list(map(int, input().split()))) #Sorting the input for Bob.
	A.pop() #Removing the max time for Alice.
	B.pop() #Removing the max time for Bob.
	time_A, time_B = sum(A), sum(B) #Total time taken by both.
	if time_A == time_B:
		print('Draw')
	else:
		result = 'Alice' if min(time_A, time_B) == time_A else 'Bob'
		print(result)