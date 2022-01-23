a,b,c,d,e,f = map(int,input().split())
num_list = [a,b,c,d,e,f]
N = int(input())

for i in range(N):
    count = 0
    g,h,i,j,k,l = map(int,input().split())
    num_list1 = [g,h,i,j,k,l]
    num_list2 = sorted(num_list1)
    for num in num_list2:
        if num in num_list:
            count += 1
    print(count)
    