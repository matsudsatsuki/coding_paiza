from itertools import product
import re
n,m = map(int,input().split())
A = []
AA = []
for _ in range(m):
    a = input()
    num = re.findall(r"\d+", a)
    if 'honest' in a:
        AA.append([[int(num[0])-1,int(num[1])-1],True])
    if 'liar' in a:
        AA.append([[int(num[0])-1,int(num[1])-1],False])

#print(AA)
A.append(AA)
#print(AA)

def judge(bit):
    for i in range(n):
        if not (bit&(1<<i)):
            continue
        for x,y in AA:
            if y == True and not (bit&(1<<int(x[0]))):
                return False
            if y == False and bit&(1<<int(x[0])):
                return False
    return True
    
ans = 0
        
for bit in range(1<<n):
    if judge(bit):
        count = 0
        ans += 1
        for i in range(n):
            if bit & (1<<i):
                count += 1

if count == 0:
    print(-1)
    exit()
if ans == 1:
    print(1)
else:
    b = format(ans,'b')
    print(len(b))
    