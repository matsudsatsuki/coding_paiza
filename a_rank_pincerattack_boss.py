
#answer
H,W,N,n = map(int,input().split())

S = [list(input())for i in range(H)]
points = [list(map(int,input().split()))for i in range(n)]

def check_diagnol(x,y,S,player):
    for lr1 in range(-1,2,2):
        for lr2 in range(-1,2,2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                    ):
                        break
                if S[y+i*lr2][x+i*lr1] == player:
                    for j in range(i+1):
                        S[y+j*lr2][x+j*lr1] = player
                    break
                if S[y+i*lr2][x+i*lr1] == '#':
                    break

def check_row(x,y,S,player):
    for lr in range(-1,2,2):
        i = 0
        while True:
            i += 1
            if x+i*lr < 0 or x+i*lr >= W:
                break
            if S[y][x+i*lr] == player:
                for j in range(i+1):
                    S[y][x+j*lr] = player
                break
            if S[y][x+i*lr] == '#':
                break
                    
def check_column(x,y,S,player):
    for lr in range(-1,2,2):
        i = 0
        while True:
            i += 1
            if y+i*lr < 0 or y+i*lr >= H:
                break
            if S[y+i*lr][x] == player:
                for j in range(i+1):
                    S[y+j*lr][x] = player
                break
            if S[y+i*lr][x] == '#':
                break
            
for p,y,x in points:
    S[y][x] = p
    check_row(x,y,S,p)
    check_column(x,y,S,p)
    check_diagnol(x,y,S,p)
    
for y in range(H):
    for x in range(W):
        print(S[y][x],end='')
    print()
    
    