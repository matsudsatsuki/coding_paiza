n = int(input())
a = list(int(input()) for i in range(n))

ans_sum = 0
for i in range(n):
    if a[i] >= 5:
        ans_sum += a[i]
    else:
        continue

print(ans_sum)