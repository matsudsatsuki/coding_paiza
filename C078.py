#failed(continueとbreakを間違えた)
N,c_1,c_2 = map(int,input().split())
stock = 0
profit = 0
close_price = 0
for day in range(N):
    price = int(input())
    if price > c_1 and price < c_2 and day != N-1:
        break#continueにするとsuccess
    if day == N-1:
        profit += stock*price
        break
    if price <= c_1:
        stock += 1
        profit -= price
    if price >= c_2:
        profit += stock*price
        stock = 0
print(profit)
    
