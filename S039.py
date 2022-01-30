H,W = map(int,input().split())

S = [list(input())for j in range(H)]
print(S)

ans = 0
ans_list = []

def check_dimention(S,y,x,n):
    if S[y][x] == '#':
        return n
    else:
        n += 1
        return check_dimention(S,y+1,x+1,n)

flag = False
for y in range(H):
    for x in range(W):
        matrix = 1
        if x < W-1 and y < H-1 and S[y][x] == '.':
            if S[y+1][x+1] == '.':
                for step in range(1,matrix+1):
                        if '#' not in S[y+1][x+1-step] and '#' not in S[y+1-step][x+1]:
                            flag = True
                elif flag = False and '#' not in S[y+1][x+1-step]:
                    while True:
                        if '#' not in S[y+1][x+1-step]:
                            ans += matrix 
                            y += 1
                        else:
                            break
                    ans_list.append(ans)
                elif flag = False and '#' not in S[y+1-step][x+1]:
                    while True:
                        if '#' not in S[y+1-step][x+1]:
                            ans += matrix 
                            x += 1
                        else:
                            break
                    ans_list.append(ans)
                            
                if flag:
                    matrix += 1
                    ans = matrix**2
                    ans_list.append(ans)
                    y += 1
                    x += 1
                    
                        
                        
            elif S[y][x] == '#':
                continue
            else:
                break