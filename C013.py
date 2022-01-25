hate_num = input()
N = int(input())
flag = True
for i in range(N):
    A = input()
    for num in A:
        if hate_num not in A:
            print(A)
            flag=False
            break
        
if flag:
    print('none')