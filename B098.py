N,M,T,K = map(int,input().split())

sumple = [list(map(int,input().split()))for i in range(M)]
time_flag = []
cum_sum = 0
ans_list = []
for i in range(N):
    ans_list.append(0)
#print(sumple[3][1])
for i in range(N):
    for j in range(M-T):
        cum_sum = 0
        for k in range(T):
            cum_sum += sumple[j+k][i]
            if cum_sum >= K:
                time_flag=j+k+1
                print(time_flag)
                cum_sum=0
                ans_list[i] = time_flag
                