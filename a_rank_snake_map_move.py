H,W,sy,sx,N = map(int,input().split())

S = [list(input())for i in range(H)]
time_lr = [input().split()for i in range(N)]
steps = []
directions = []
sy = int(sy)
sx = int(sx)
directions = ['N','E','S','W']
now_directions = 0
time_index = 0

for t_now in range(100):
    if str(t_now) == time_lr[time_index][0]:
        d = time_lr[time_index][1]
        time_index += 1
        if d == 'L':
            now_directions = (3+now_directions)%4
        else:
            now_directions = (1+now_directions)%4
    
    if directions[now_directions] == 'N':
        sy -= 1
    elif directions[now_directions] == 'E':
        sx += 1
    elif directions[now_directions] == 'S':
        sy += 1
    elif directions[now_directions] == 'W':
        sx -= 1
        
    if sx < 0 or sx >= int(W) or sy < 0 or sy >= int(H) or S[sy][sx] == '#':
        print('Stop')
        break
    else:
        print(sy,sx)
