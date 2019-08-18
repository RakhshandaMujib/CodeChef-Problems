T = int(input())
for i in range(T):
    num = input()
    count = 0
    for j in range(len(num)):
        if num[j] == '4':
            count += 1
    print(count)
