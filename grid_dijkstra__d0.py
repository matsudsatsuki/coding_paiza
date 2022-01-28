H,W = map(int,input().split())
S = [list(map(int,input().split()))for i in range(H)]

dx = [1,0,1,0,-1]
dy = [0,1,0,-1,0]
init_x = 0
init_y = 0
ans = 0
for i in range(5):
    ny = init_y+dy[i]
    nx = init_x+dx[i]
    ans += S[ny][nx]
    init_y += dy[i]
    init_x += dx[i]
    
print(ans)