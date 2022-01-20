H,W,r,c = map(int,input().split())

S = [list(input())for i in range(H)]

if S[r-1][c-1] == '.':
    print('No')
else:
    print('Yes')