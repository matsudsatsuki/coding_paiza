# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import itertools 
A = input()
B = input()
S = input()
dust_list = 0
counter = 0
#bb = B.find(S[0])
#cc = B[bb+1:]
#print(cc)
def check__shortest(A,B,S):
    for a,b in itertools.zip_longest(A,B):
        if S == a and S == b:
            continue
            
        if S == a and S != b:
            return B
            #index = B.find(S)
            #B = B[index+1:]
            break
        if S == b and S != a:
            return A
            break
            
            
            
            
#bb,ans = check_num(A,B,S[0])
#print(bb,ans)
dyn_A = A
dyn_B = B
ans = 0
shortest_A = 0
shortest_B = 0
j = 0
flag = True
for i in range(len(S)):
    flag = True
    if dyn_A.find(S[i])==dyn_B.find(S[i]):
        flag = False
        ans += 1
        loc = dyn_A.find(S[i])
        j = i+1
        while j < len(S)-1:
            j += 1
            if check__shortest(dyn_A,dyn_B,S[j]) == dyn_A:
                index = loc
                dyn_A = dyn_A[index+1:]
                #print('A')
                break
            if check__shortest(dyn_A,dyn_B,S[j]) == dyn_B:
                index = loc
                dyn_B = dyn_B[index+1:]
                #print('B')
                break
            if check__shortest(dyn_A,dyn_B,S[j]):
                continue
        
                
            
               
                
    
    elif flag:
        for a,b in itertools.zip_longest(dyn_A,dyn_B):
            if S[i] == a:
                #print('first')
                index = dyn_A.find(S[i])
                ans += index+1
                dyn_A = dyn_A[index+1:]
                #print(ans)
                break
            if S[i] == b:
                index = dyn_B.find(S[i])
                ans += index+1
                dyn_B = dyn_B[index+1:]
                #print(ans)
                break
                
    #print(i)
  
  
print(ans)
