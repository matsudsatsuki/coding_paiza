N = int(input())
sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
q = []
q.append((tx,ty))
#print(q)
ans_list = []

def around_checker(sx,sy,tx,ty):
    if sx+1 == tx:
        if sy-1 == ty or sy == ty or sy+1 == ty:
            return True
    if sx-1 == tx:
        if sy-1 == ty or sy == ty or sy+1 == ty:
            return True
    if sx == tx:
        if sy-1 == ty or sy+1 == ty:
            return True
    else:
        return False
    #if tx == sx+1
dust_list = []  
catched = set()
count = 0
time = 1
time_list = []
time_list.append([sx,sy])
step = 0
init_x = sx
init_y = sy
#for x,y in q:
    #print(x,y)
while True:
    #op_x,op_y = q.pop()
    count += 1
    time += 1
    flag = True
    sx = init_x
    sy = init_y
    for op_x,op_y in q:
        if sx < op_x and sy > op_y and flag:
            sx += 1
            sy -= 1
            flag = False
        #if sx + 1 == op_x and sy == op_y:
            #if op_x + 1 > N-1:
                #ans_list.append(count+1)
        if sx < op_x and sy < op_y and flag:
            sx += 1
            sy += 1
            flag = False
        #if sx + 1 == op_x and sy == op_y:
            #if op_x + 1 > N-1: #ans_list.append(count+1)
        
        if sx > op_x and sy > op_y and flag:
            sx -= 1
            sy -= 1
            flag = False
        #if sx -1 == op_x and sy == op_y:
            #if op_x-1 < 0: #ans_list.append(count+1)
                
        if sx > op_x and sy < op_y and flag:
            sx -= 1
            sy += 1
            flag = False
        #if sx -1 == op_x and sy == op_y:
            #if op_x-1 < 0:
                 #ans_list.append(count+1)
         
        if sx == op_x and flag:
            if sy < op_y:
                sy += 1
                flag = False
            #
        if sy > op_y and flag:
            sy -= 1
            flag = False
            #if sx == op_x and sy-1 == op_y:
                #if op_y-1 < 0:
                     #ans_list.append(count+1)
        if sy == op_y and flag:
            if sx < op_x:
                sx += 1
                flag = False
            #if sy == op_y and sx+1 == op_x:
                #if op_x+1 > N-1:
                     #ans_list.append(count+1)
        if sx > op_x and flag:
            sx -= 1
            flag = False
            init_x = sx
            init_y = sy
        if op_x+1 < N and op_y-1 >= 0:
            q.append((op_x+1,op_y-1))
        #print(q)
            if around_checker(sx,sy,op_x+1,op_y-1):
                dust_list = q.pop()
                ans_list.append(count+1)
        if op_x+1 < N and op_y+1 < N:
            q.append((op_x+1,op_y+1))
        #print(q)
            if around_checker(sx,sy,op_x+1,op_y+1):
                dust_list = q.pop()
                ans_list.append(count+1)
        if op_x-1 >= 0 and op_y-1 >= 0:
            q.append((op_x-1,op_y-1))
        #print(q)
            if around_checker(sx,sy,op_x-1,op_y-1):
                dust_list = q.pop()
                ans_list.append(count+1)
        if op_x-1 >= 0 and op_y+1 < N:
            q.append((op_x-1,op_y+1))
        #print(q)
            if around_checker(sx,sy,op_x-1,op_y+1):
                dust_list = q.pop()
                ans_list.append(count+1)
    break
    
        
        
  
   
    
print(max(ans_list))