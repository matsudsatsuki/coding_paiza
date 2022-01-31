#submit
import itertools
N = int(input())

num_list = []
n = 0
for i in range(N):
    n = int(input())
    num_list.append(n)

#print(num_list)
sum_list = list(itertools.combinations(num_list,3))
#print(len(sum_list))
count = 0
for i in sum_list:
    if sum(i) % 7 == 0:
        count += 1
print(count)

#answer
n = int(input())

a = [0] * 7
for _ in range(n):
    a[int(input()) % 7] += 1

mod7 = []
for i in range(7):
    for j in range(i, 7):
        for k in range(j, 7):
            if (i + j + k) % 7 == 0:
                mod7.append((i, j, k))

ans = 0
for group in mod7:
    i, j, k = group
    if i == j == k:
        ans += a[i] * (a[i] - 1) * (a[i] - 2) // 6
    elif i == j:
        ans += a[i] * (a[i] - 1) * a[k] // 2
    elif j == k:
        ans += a[i] * a[j] * (a[j] - 1) // 2
    elif k == i:
        ans += (a[k] - 1) * a[j] * a[k] // 2
    else:
        ans += a[i] * a[j] * a[k]

print(ans)