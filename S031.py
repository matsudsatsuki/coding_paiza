N,budget,max_pipe = map(int,input().split())

    
def cal_max_iter(pipe_price,pipe_bar,budget,use_items):
    n = use_items
    m = [[0]*(budget+1)for i in range(n+1)]#最大値を格納する配列
    P = [[False]*(budget+1)for i in range(n+1)]#選択過程を格納する配列
    add_list = []
    for k in range(1,n+1):
        i = k-1
        for r in range(1,budget+1):#予算内に収まるかどうか
            drop = m[k-1][r]        
            m[k][r] = drop
            if pipe_price[i] > r : continue
            keep = pipe_bar[i] + m[k-1][r-pipe_price[i]]
            m[k][r] = max(drop,keep)
            P[k][r] = keep > drop 
            if P[k][r] and k == n-1:
                add_list.append(pipe_bar[i])
                
    return m,P,add_list
    
    
pipe_list = []
price_list = []
    
for i in range(N):
    pipe,price = map(int,input().split())
    pipe_list.append(pipe)
    price_list.append(price)
    
#print(price_list)
m,P,add_l = cal_max_iter(price_list,pipe_list,budget,N)
k,r,items = N,budget,set()
while k > 0 and r > 0:
    i = k-1
    if P[k][r]:
        items.add(i)
        r -= price_list[i]
    k -= 1
    
    
#print(m)
item_list = list(items)
ans_list = []
for item in item_list:
    ans_list.append(pipe_list[item])
    

#print(P)
print(min(ans_list))
