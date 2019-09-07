for _ in range(int(input())):
    l = list(map(int, input().split()))
    z = sorted(zip(l[:3], l[3:])) #Coupling the age and eidi.
    flag = True
    for i in range(2):	
        if z[i][0] == z[i+1][0] and z[i][1] != z[i+1][1] or \
           z[i][0] < z[i+1][0] and z[i][1] >= z[i+1][1]:
            flag = False
            break
    if flag:
        print("FAIR")
    else:
        print("NOT FAIR")