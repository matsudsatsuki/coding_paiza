N,D = map(int,input().split())
d = 0
row = 0
for i in range(N-1):
    d = int(input())
    row += D-d

ans = D * (row+D)

print(ans)