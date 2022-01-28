#submit(failed)
W,H = map(int,input().split())
G = [list(input().split())for i in range(H)]
#print(G)
init_y = 0
init_x = 0
goal_y = 0
goal_x = 0
for y in range(H):
    for x in range(W):
        if G[y][x] == 's':
            init_y = y
            init_x = x
        if G[y][x] == '0':
            G[y][x] = 1
        if G[y][x] == '1':
            G[y][x] = 2
        if G[y][x] == 'g':
            goal_y = y
            goal_x = x

import heapq

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.cost < other.cost


def dijkstra(h, w, t, sx, sy, gx, gy):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    initial_state = State(sx, sy, 0)
    heapq.heappush(open_list, initial_state)

    while open_list:
        st = heapq.heappop(open_list)

        if st.x == gx and st.y == gy:
            return st.cost
        if st in closed:
            continue
        #print(st.x,st.y)

        closed.add(st)

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]
            #print(ny,nx)
            if t[ny][nx] == 1 and not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue
            else:
                break
            ncost = st.cost+t[ny][nx]
            heapq.heappush(open_list, State(nx, ny, ncost))
            

    return 'Fail'


cost = dijkstra(H,W,G,init_x,init_y,goal_x,goal_y)


print(cost)