N,K,M = map(int,input().split())
words_list = []
for i in range(K):
    words = input()
    words_list.append(words)

survive = N
talk_list = []

for i in range(M):
    talk = input()
    talk_list.append(talk)
players = [0]*N

words_list.remove(talk_list[0])
for i in range(1,M):
    if talk_list[i] in words_list and talk_list[i][-1] != 'z':
        if talk_list[i-1][-1] == talk_list[i][0]:
            words_list.remove(talk_list[i])
        else:
            continue
            
            
            
    else:
        players[i%survive] = 1
        survive -= 1
        if talk_list[i] in words_list:
            words_list.remove(talk_list[i])
    
print(survive) 
for i in range(N):
    if players[i] == 0:
        print(i+1)
        