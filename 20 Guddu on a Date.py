for _ in range(int(input())):
    N = int(input()) #Read the input.
    s = lambda n: sum([int(x) for x in str(n)]) #N -> str -> list of int -> sum 
    add = 0 if not (s(N) % 10) else (10 - (s(N) % 10))
    print(10 * N + add)