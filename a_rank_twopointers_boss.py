N,K = map(int,input().split())
S = list(map(int,input().split()))
cum_mul = S[0]
ans = 10000
count = 1
for i in range(N):
    j = i+1
    for j in range(N-1):
        if cum_mul >= K:
            break
        else:
            count += 1
            cum_mul *= S[j]
    ans = min(ans,count)  
        
        
    

print(ans)