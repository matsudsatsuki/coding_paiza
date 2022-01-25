#submit
n,k = map(int,input().split())

days = list(map(int,input().split()))
ave = [None]*(n-k+1)

for i in range(n-k+1):
    ave[i] = sum(days[i:k+i])
    
m = max(ave)
print(ave.count(m),ave.index(m)+1)

#answer
n, k = map(int, input().split())
data = list(map(int, input().split()))

ave = [None] * (n - k + 1)
ave[0] = sum(data[:k])

for i in range(1, n - k + 1):
    ave[i] = ave[i - 1] - data[i - 1] + data[i - 1 + k]

m = max(ave)

print(ave.count(m), ave.index(m) + 1)