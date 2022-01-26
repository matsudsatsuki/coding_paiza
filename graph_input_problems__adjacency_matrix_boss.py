n,q = map(int,input().split())
G = [[int(j)for j in input().split()]for i in range(n)]

for i in range(q):
    x,y = map(int,input().split())
    print(G[x-1][y-1])
        
            