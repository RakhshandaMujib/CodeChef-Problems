def partner(seat):
	seat_type = {0:'SL', 1:'LB', 2:'MB', 3:'UB', 4:'LB', 5:'MB', 6:'UB', 7:'SU'}
	l1 = [1,2,3]
	l2 = [4,5,6]
	partner = 0
	if seat % 8 == 0:
		partner = seat - 1
	elif seat % 8 in l1:
		partner = seat + 3
	elif seat % 8 in l2:
		partner = seat - 3
	elif seat % 8 == 7:
		partner = seat + 1
	return str(partner) + seat_type[seat % 8]

for _ in range(int(input())):
	seat = int(input())
	print(partner(seat))
