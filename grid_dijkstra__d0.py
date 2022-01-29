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

#answer
h, w = map(int, input().split())
t = [[int(x) for x in input().split()] for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
r, u, l, d = range(4)

x, y = 0, 0
cost = t[y][x]

x += dx[r]
y += dy[r]
cost += t[y][x]

x += dx[d]
y += dy[d]
cost += t[y][x]

x += dx[r]
y += dy[r]
cost += t[y][x]

x += dx[u]
y += dy[u]
cost += t[y][x]

x += dx[l]
y += dy[l]
cost += t[y][x]

print(cost)