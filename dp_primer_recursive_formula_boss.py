#submit(time_limit_exceeded)
Q = int(input())

def fibo(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


for i in range(Q):
    a = int(input())
    print(fibo(a-1))

#answer
a = [1] * (40 + 1)

for i in range(3, 40 + 1):
    a[i] = a[i - 1] + a[i - 2]

q = int(input())

for i in range(q):
    k = int(input())
    print(a[k])