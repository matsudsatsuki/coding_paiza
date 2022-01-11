M = int(input())
a = list(int(input()) for i in range(M))
N = int(input())
b = list(int(input()) for i in range(N))
flag = 0


for i in range(1,32):
    if i in a and i in b:
        if flag == 0:
            print('A')
            flag = 1
        else:
            print('B')
            flag = 0
    elif i in a:
        print('A')
    elif i in b:
        print('B')
    else:
        print('x')
    