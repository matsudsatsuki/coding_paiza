xc,yc,r_1,r_2 = map(int,input().split())
N = int(input())

def check(x,y):
    if (x-xc)**2 + (y-yc)**2 <= r_2**2 and (x-xc)**2 + (y-yc)**2 >= r_1**2:
        return True

for i in range(N):
    x, y = input().split()
    if check(int(x),int(y)):
        print('yes')
    else:
        print('no')