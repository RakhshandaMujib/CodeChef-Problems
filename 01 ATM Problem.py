l = input().split()
amount, balance = int(l[0]), float(l[1])
if amount % 5 == 0 and (amount + 0.5) <= balance:
	balance -= (amount + 0.5)
print("%.2f"%balance)
