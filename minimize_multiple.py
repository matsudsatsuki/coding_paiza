A,B = map(int,input().split())

if A <= 0 and B >= 0:
    ans = A * B
elif A >= 0:
    ans = A*A
else:
    ans = B*B


    
print(ans)