#my answer
H,W = map(int, input().split())
S = [list(input())for i in range(H)]

for y in range(H):
    for x in range(W):
        if y == 0 or S[y-1][x] == '#':
            if y == H-1 or S[y+1][x] == '#':
                if x == 0 or S[y][x-1] == '#':
                    if x == W-1 or S[y][x+1] == '#':
                        print(y,x)

#answer
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        flag_row = False
        flag_column = False

        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                flag_row = True

        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                flag_column = True

        if flag_column and flag_row:
            print(y, x)