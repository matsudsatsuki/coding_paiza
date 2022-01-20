N = int(input())
A = [int(i)for i in input().split()]
B = [int(i) for i in input().split()]


C = set(A+B)
ans = sorted(C)
print(' '.join(map(str,ans)))
