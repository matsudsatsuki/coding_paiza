from collections import deque
N = int(input())
num_list = [int(x) for x in input().split()]
div_list = [[]for i in range((N//3)+1)]
#print(num_list)
#print(len(div_list))

output=[num_list[i:i + 3] for i in range(0, len(num_list), 3)]

def is_sorted(l):
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return True
    else:
        return False
        
def is_reverse(l):
    if l == sorted(l,reverse=True):
        return True
    else:
        return False
#print(is_reverse([2,3,1]))
turn = 1
n = len(output)
count = 0
q = deque(output)
#b = q.popleft()
#print(b)
new_list = []
while q:
    b = q.popleft()
    #print(b)
    #print(new_list)
    if is_sorted(b):
        new_list.append(b[0])
        #print('aa')
        continue
    if is_sorted(b) == False and is_reverse(b):
        count += 2
        b = sorted(b)
        new_list.append(b[0])
        #print('a')
    if is_sorted(b) == False and is_reverse(b) == False:
        count += 1
        b = sorted(b)
        new_list.append(b[0])
        #print('b')
    if len(new_list) > 2 and is_sorted(new_list) == False:
        q.append(new_list)
        #print('c')
    if len(new_list) == 1:
        #print('d')
        continue
    if len(new_list) == 2:
        if new_list[0] > new_list[1]:
            #print('e')
            count += 1
            break
        else:
            #print('f')
            break
            
    
    #print(new_list)
    
#for i in num_list:
print(count)




#for i in range(n):
    #if is_sorted(output[i]):
        #continue
    #if is_sorted(output[i]) == False and is_reverse(output[i]):
        #count += 2
        #output[i] = sorted(output[i])
        #flag = False
    #if is_sorted(output[i]) == False and is_reverse(output[i]) == False:
        #count += 1
        #output[i] = sorted(output[i])
        #flag = False
    