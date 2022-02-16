import collections
N = int(input())
word_list = []
m = 0
for i in range(N):
    a = input()
    m = max(len(a),m)
    word_list.append(a)

count = 0
pref_list = []
ans_list = []
#print(m)
for i in range(-1,-(m+1),-1):
    for j in range(N):
        #print('a')
        pref_list.append(word_list[j][i:])
    c = collections.Counter(pref_list)
    prefix = list(c.keys())
    sames = list(c.values())
    count += 1
    ans_list.append((sames[0]-1)*count)
    del pref_list[:]
    
print(max(ans_list))
#print(ans_list)