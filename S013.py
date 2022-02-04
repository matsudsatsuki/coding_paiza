N = int(input())
cost_to_future,cost_to_past = map(int,input().split())

safe = input()
safe_list = []
for i in safe:
    safe_list.append(i)
#print(safe_list)
safe_dict = {x: safe_list[x-1] for x in range(1,N+1)}
#print(safe_dict)
q = []
q.append((N,safe_dict[N]))
#print(q[0][0])
travel_his = set()
cost = 0
count = 0
ans_list = []
while q:
    st = q.pop()
    count += 1
    ans_list.append(st[0])
    if st in travel_his:
        continue
    travel_his.add(st)
    #print(st[0])
    #print(travel_his)

    for i in range(1,N):
        if (i,safe_dict[i]) not in travel_his:
            if safe_dict[i] == 's':
                q.append((i,safe_dict[i]))
            elif st[0] > i:
                cost += cost_to_past
                break

                

    if count >= N-1 and st in travel_his:
        if safe_dict[N] == 's':
            ans_list.append(N)
            break
        elif cost_to_past > cost_to_future:
            ans_list.append(N-1)
        else:
            ans_list.append(1)
                    

    print(safe_dict)
    for j in range(i,N+1):
        if safe_dict[j] == 'd':
            safe_dict[j] = 's'
            continue
        if safe_dict[j] == 's':
            safe_dict[j] = 'd'
            continue
        if j == N+1:
            break
                
    
            
print(ans_list)
