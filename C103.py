N,M = map(int,input().split())

#actions = [list(input().split())for i in range(M)]
#print(actions[1][0])
times = []
actions = []
outputs = []
for i in range(M):
    num, action = input().split()
    num = int(num)
    times.append(num)
    actions.append(action)
    
a = [i for i in range(N+1)]

for i in range(1,N+1):
    for j in range(M):
         if a[i] % int(times[j]) == 0:
             a[i] = actions[j] 
         else:
             continue
#give up
        
   