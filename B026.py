y_500,y_100,y_50,y_10 = map(int,input().split())
N = int(input())

stock = [y_500,y_100,y_50,y_10]
#print(stock)
stock_left = []
for i in range(N):
    pay,y_500_in,y_100_in,y_50_in,y_10_in = map(int,input().split())
    pay_back = (y_500_in*500 + y_100_in*100 + y_50_in*50 + y_10_in*10) - pay
    if pay_back > 500*stock[0] and stock[0] != 0:
        pay_back -= 500*stock[0] 
        stock[0] -= 1
        print(stock)
        if pay_back > 100*stock[1] and stock[1] != 0:
            pay_back -= 100*stock[1]
            stock[1] -= 1
            print(stock) 
            if pay_back > 50*stock[2] and stock[2] != 0:
                pay_back -= 50*stock[2]
                stock[2] -= 1
                print(stock) 
                if pay_back > 10*stock[3] and stock[3] != 0:
                    pay_back -= 10*stock[3]
                    stock[3] -= 1
                    print(stock)
    else:
        print('impossible')