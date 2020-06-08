for _ in range(int(input())): 
	N = int(input())
	songs = list(map(int, input().split()))
	uncle_johnny = songs[int(input())-1]
	print(sorted(songs).index(uncle_johnny) + 1)