def is_even(x):
	'''
	Argument: 
		x- An integer.
	Returns: 
		Boolean- True, is x is an even number.
	'''
	if x%2 == 0:
		return True

def count_evens(minX, maxX, n):
	'''
	Arguments: 
		minX- An integer. The lower limit of the IDs.
		maxX- An integer. The upper limit of the IDs.
		n- An integer. Total number of elements in [minX, maxX].
	Returns: 
		Integer- Total number of even terms in [minX, maxX].
	'''
	if is_even(minX) and is_even(maxX):
		return (n // 2) + 1
	else: 
		return n // 2 

def nature(a_list):
	'''
	Argument: 
		a_list- A list of lists of weights and biases. 
	Returns:
		a_list- A list of lists with the nature of weights and biases.

	The input list is of the form [[w1,b1], [w2,b2], ...]. This method is going
	to detemine the nature of each [wi,bi] pair- whether its odd or even and 
	return a list which looks like [['o','e'], ['e','o']...]. 
	'''
	for item in a_list:
		item[0] = 'e' if is_even(item[0]) else 'o'
		item[1] = 'e' if is_even(item[1]) else 'o'
	return a_list 

def main():
	for _ in range(int(input())): #No. of test cases.
		N, minX, maxX = map(int, input().split()) 
		weight_bias = [] #A list of lists: [[w1,b1], [w2,b2]...].
		for _ in range(N): 
			weight, bias = map(int, input().split()) 
			weight_bias.append([weight, bias])

		n = maxX - minX + 1 #n = the total number of IDs.
		even_terms = count_evens(minX, maxX, n) # No. of even IDs.
		weight_bias = nature(weight_bias) #Convert to [odd, even] form.
	
		result = [] #A list of result (no. of evens) for each layer.
		for w_b in weight_bias: 
			if w_b == ['e', 'e']: 
				result.append(n) #No. of even terms = n.
			if w_b == ['e','o']: 
				result.append(0) #No. of even terms = 0.
			if w_b == ['o','e']: 
				if len(result) == 0: #In case [w1,b1] is ['o','e'].
					result.append(even_terms) #No. of even terms = even_terms.
				else:
					result.append(result[-1]) #No. of even terms = the same as 
											  #the last for the last [w,b] pair.
			if w_b == ['o', 'o']: 
				if len(result) == 0: #In case [w1,b1] is ['o','o'].
					result.append(n - even_terms) #The even terms are 
												  #going to flip from the 
												  #original in this case. 
				else:
					result.append(n - result[-1]) #The even terms are going to
												  #flip from the ones for the 
												  #last [w,b] pair.
		print(result[-1], (n - result[-1]))

if __name__ == '__main__':
	main()