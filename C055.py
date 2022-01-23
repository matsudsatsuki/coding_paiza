N = int(input())
G = input()
flag = 0
for i in range(N):
    strings = input()
    if G in strings:
        print(strings)
        flag = 1
    if flag == 0 and i == N-1 and G not in strings:
        print('None')
    
