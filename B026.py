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

#投入される金額もリストに入れて、繰り返す方がいいかも
y_500,y_100,y_50,y_10 = map(int,input().split())
N = int(input())
stock = [y_500,y_100,y_50,y_10]
yen = [500,100,50,10]
y_pay_back = []
for i in range(N):
    pay,y_500_in,y_100_in,y_50_in,y_10_in = map(int,input().split())
    pay_list = [y_500_in,y_100_in,y_50_in,y_10_in]
    pay_back = (pay_list[0]*500 + pay_list[1]*100 + pay_list[2]*50 + pay_list[3]*10) - pay
    y_pay_back = [0,0,0,0]
    for j in range(4):
        stock[j] += pay_list[j]
    if pay_back > 500 and stock[0] >= pay_back//500:
        stock[0] -= pay_back//500
        y_pay_back[0] = pay_back//500
        pay_back -= 500*(pay_back//500)
        if pay_back != 0 and pay_back > 100 and stock[1] >= pay_back//100:
            stock[1] -= pay_back//100
            y_pay_back[1] = pay_back//100
            pay_back -= 100*(pay_back//100)
            if pay_back != 0 and pay_back > 50 and stock[2] >= pay_back//50:
                stock[2] -= pay_back//50
                y_pay_back[2] = pay_back//50
                pay_back -= 50*(pay_back//50)
                if pay_back != 0 and pay_back > 10 and stock[3] >= pay_back//10:
                    stock[3] -= pay_back*10
                    y_pay_back[3] = pay_back//10
                    pay_back -= 10*(pay_back//10)
                    if pay_back != 0:
                        print('impossible')
                    else:
                        print(y_pay_back[0],y_pay_back[1],y_pay_back[2],y_pay_back[3])
                        
    elif pay_back != 0 and pay_back > 100 and stock[1] >= pay_back//100:
        stock[1] -= pay_back//100
        y_pay_back[1] = pay_back//100
        pay_back -= 100*(pay_back//100)
        if pay_back != 0 and pay_back > 50 and stock[2] >= pay_back//50:
            stock[2] -= pay_back//50
            y_pay_back[2] = pay_back//50
            pay_back -= 50*(pay_back//50)
            if pay_back != 0 and pay_back > 10 and stock[3] >= pay_back//10:
                stock[3] -= pay_back//10
                y_pay_back[3] = pay_back//10
                pay_back -= 10*(pay_back//10)
                if pay_back != 0:
                    print('impossible')
                else:
                    print(y_pay_back[0],y_pay_back[1],y_pay_back[2],y_pay_back[3])
                    
    elif pay_back != 0 and pay_back > 50 and stock[2] >= pay_back//50:
        stock[2] -= pay_back//50
        y_pay_back[2] = pay_back//50
        pay_back -= 50*(pay_back//50)
        if pay_back != 0 and pay_back > 10 and stock[3] >= pay_back//10:
            stock[3] -= pay_back//10
            y_pay_back[3] = pay_back//10
            pay_back -= 10*(pay_back//10)
            if pay_back != 0:
                print('impossible')
            else:
                print(y_pay_back[0],y_pay_back[1],y_pay_back[2],y_pay_back[3])
                
    elif pay_back != 0 and pay_back > 10 and stock[3] >= pay_back//10:
        stock[3] -= pay_back//10
        y_pay_back[3] = pay_back//10
        pay_back -= 10*(pay_back//10)
        if pay_back != 0:
            print('impossible')
        else:
            print(y_pay_back[0],y_pay_back[1],y_pay_back[2],y_pay_back[3])
    
    else:
        print('impossible')
            
   
                    