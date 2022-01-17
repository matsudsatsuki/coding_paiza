N,M = map(int,input().split())
rows = [list(map(int,input().split()))for i in range(N)]
flag_list = []
for i in range(N):
    flag_list.append(0)

for i in range(N):
    for j in range(N):
        if rows[i][j] >= M:
            flag_list[j] = 1
        else:
            continue


#for i in range(N):
    #ans_list.append(0)
ans_list = []
#print(ans_list)

for i in range(N):
    if 0 not in flag_list:
        print('wait')
        break
    elif flag_list[i] == 0:
        ans_list.append(i+1)
        if i == N-1:
            print(*ans_list,sep=' ')
    else:
        continue

#score 70