#Check out the commented version (14-41) for the detailed working of the code below (3-11):

for _ in range(int(input())):
	N = int(input())
	S = input()	
	lst_1 = [S[i-1] if i%2 else (S[i+1] if i!= N-1 else S[i]) for i in range(N)]
	first_encoding = ''.join(lst_1)
	lst_2 = []
	for letter in first_encoding.lower():
		lst_2.append(chr(ord(letter) + 25 - 2 * (ord(letter) % 97)))
	print(''.join(lst_2))

'''
def swap_letters(S, N):
	#To swap the letters:
	  #1) Run a loop from 0 to N.
	  #2) If the index is EVEN, append the (index - 1)th
	  #   to the list.
	  #3) If the index is ODD, check:
	  	   #If the index is NOT at the end of the list: 
	  	     #If no, meaning the index points to the last element, 
	  	       #append it as it is to the list (this takes care of 
	  	       #odd-lenght strings).
	  	     #If yes, meaning the index DOESN'T point to the last 
	  	       #element, append (index + 1)th letter to the list 
	  	       #(works for letters at the even positions).
	lst = [S[i-1] if i%2 else (S[i+1] if i!= N-1 else S[i]) for i in range(N)]
	return ''.join(lst)

def invert_letters(S):
	lst = []
	for letter in S.lower():
		lst.append(chr(ord(letter) + 25 - 2 * (ord(letter) % 97)))
	return ''.join(lst)

for _ in range(int(input())):
	N = int(input())
	S = input()	
	first_encoding = swap_letters(S, N)
	second_encoding = invert_letters(first_encoding)
	print(second_encoding)
'''