N,M = map(int,input().split())

table_list = [0]*N

for i in range(M):
    member,start = map(int,input().split())
    flag = True
    for j in range(start,start+member):
        if table_list[j%N] == 1:
            flag=False
            break
    if not flag:
        continue
    
    for k in range(start,start+member):
        table_list[k%N] = 1
    
print(table_list.count(1))
    