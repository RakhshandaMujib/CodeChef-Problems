for _ in range(int(input())):
    s = input().lower()
    if 'ec' in s or 'sc' in s or 'se' in s:
        print('no')
    else:
        print('yes')