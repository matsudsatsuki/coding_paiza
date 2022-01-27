W,H = map(int,input().split())
G = [list(map(int,input().split()))for i in range(H)]

count = 0
for y in range(H):
    for x in range(W):
        my_p = []
        if G[y][x] == 1:
            my_p.append([y,x])
            while my_p:
                [y,x] = my_p.pop(0)
                if y > 0 and G[y - 1][x] == 1:
                    G[y - 1][x] = 0
                    my_p.append([y - 1, x])
                if y < H - 1 and G[y + 1][x] == 1:
                    G[y + 1][x] = 0
                    my_p.append([y + 1, x])
                if x > 0 and G[y][x - 1] == 1:
                    G[y][x - 1] = 0
                    my_p.append([y, x - 1])
                if x < W - 1 and G[y][x + 1] == 1:
                    G[y][x + 1] = 0
                    my_p.append([y, x + 1])
                if not my_p:
                    count += 1
                    
print(count)
        
#answer
m, n = map(int, input().split())
atlas = [input().split() for _ in range(n)]

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
for i in range(len(atlas)):
    for j in range(len(atlas[y])):
        if atlas[i][j] == "0":
            continue

        ans += 1
        q = [(i, j)]
        while q:
            y, x = q.pop(0)
            atlas[y][x] = "0"
            for vec in move:
                next_y = y + vec[0]
                next_x = x + vec[1]

                if not (0 <= next_y <= n - 1 and 0 <= next_x <= m - 1):
                    continue
                if atlas[next_y][next_x] == "0":
                    continue

                q.append((next_y, next_x))

print(ans)
        