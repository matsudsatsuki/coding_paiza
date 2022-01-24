n,r = map(int,input().split())

d = 2*r

box = [list(map(int,input().split()))for i in range(n)]

count = 0
for a,b,c in box:
    count += 1
    for i in range(n):
         if a >= d and b >= d and c >= d:
             print(count)
             break
   