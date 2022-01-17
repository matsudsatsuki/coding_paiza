N = int(input())
start = []
for i in range(N):
    start.append(int(input()))
    

M = int(input())

for i in range(M):
    pas = list(map(int,input().split()))
    if start[pas[0]-1] > pas[2]:
        start[pas[1]-1] += pas[2]
        start[pas[0]-1] -= pas[2]
    else:
        start[pas[1]-1] += start[pas[0]-1]
        start[pas[0]-1] = 0
        
    
for i in range(M):
    print(start[i])


    