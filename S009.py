import itertools

n = int(input())

num_list = [int(x) for x in input().split()]
#print(num_list)

m = int(input())
trans_list = []

for i in range(m):
    trans_list.append(list(map(int, input().split())))
index = []
for i in range(1,n+1):
    index.append(i)
    

  
num_dict = dict(zip(index,num_list))
#print(num_dict[1])
ans_dict = num_dict.copy()
#print(ans_dict)
for i in range(n):
    ans_dict[trans_list[1][i]] = num_dict[i+1]
    #print(num_dict[trans_list[1][i]])
#print(ans_dict)
perm_list = list(itertools.permutations(range(m)))#変換indexの組み合わせ

def trasform(n,dictionary,trasform_list,row):
    ans_dict = dictionary.copy()
    for i in range(n):
         ans_dict[trasform_list[row][i]] = dictionary[i+1]
    return ans_dict
    
def check(dictionary1,dictionary2):
    for i in range(len(dictionary1)):
        if dictionary1[i] == dictionary2[i]:
            continue
        if dictionary1[i] > dictionary2[i]:
            return dictionary2
        if dictionary1[i] < dictionary2[i]:
            return dictionary1
        

#b = trasform(n,num_dict,trans_list,1)       
#print(b)
#c = trasform(n,b,trans_list,0)
#print(c)
count = 0
#all_dict = {}*m
row = 0
all_list = []
a = num_dict
#print(trans_list[:m][0])
for x in perm_list:
    perm_index = list(x)
    for num in perm_index:
        if count != 0:
            if count % m == m-1:
                a = trasform(n,a,trans_list,num)
                all_list.append(a)
                print(a)
                count += 1
                break
                #print('b')
            if count % m == 0:
                a = num_dict
                a = trasform(n,a,trans_list,num)
                all_list.append(a)
                print(a)
                count += 1
                
        else:
            a = trasform(n,a,trans_list,num)
            all_list.append(a)
            print(a)
            count += 1
    
print(all_list[0])        #print('a')
            
        #row = num
        #while row < m:
            #a = trasform(n,a,trans_list,row)
            #row += 1
            #print(a)
            