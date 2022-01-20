A,B,C,D = map(int,input().split())

print(int(not ((not A and not B) or not C)) ^ int(D))