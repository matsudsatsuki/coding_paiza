n,x = map(int,input().split())

num_list = [int(input())for _ in range(n)]

dp = [False]*(x+1)
dp[0] = True

for val in num_list:
    for j in range(val,x+1):
        if dp[j-val]:
            dp[j] = True

if dp[x]:
    print('yes')
else:
    print('no')