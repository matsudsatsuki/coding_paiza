#submit
import heapq

dx = [1,0,-1,0]
dy = [0,-1,0,1]


class State:
    def __init__(self,x,y,cost,ref):
        self.x = x
        self.y = y
        self.cost = cost
        self.ref = ref
    def __hash__(self):
        return (self.x << 16) | self.y
    def __eq__(self,others):
        return self.x == others.x and self.y == others.y
    def __lt__(self,others):
        return self.cost < others.cost
    
def dijkstra(h,w,t,sx,sy,gx,gy):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    init_state = State(sx,sy,t[sy][sx],None)
    heapq.heappush(open_list,init_state)
    while open_list:
        st = heapq.heappop(open_list)
        if st.x == gx and st.y == gy:
            return st
        if st in closed:
            continue
        closed.add(st)
        
        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]
            if not (0 <= nx <= w-1 and 0 <= ny <= h-1):
                continue
            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list,State(nx,ny,ncost,st))
    return 

H,W = map(int,input().split())

T = [[int(x)for x in input().split()]for _ in range(H)]
n = int(input())
cost_list = []
st = dijkstra(H,W,T,0,0,W-1,H-1)
cost = st.cost
print(cost)
while st is not None:
    cost_list.append(T[st.y][st.x])
    st = st.ref

sorted_cost_list = sorted(cost_list)   
print(sorted_cost_list)

for i in range(n):
    a = sorted_cost_list.pop()
    cost -= a
    
print(cost)
#answer
import heapq

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


class State:
    def __init__(self, x, y, ticket, cost):
        self.x = x
        self.y = y
        self.ticket = ticket
        self.cost = cost

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.ticket == other.ticket

    def __lt__(self, other):
        return self.cost < other.cost


def dijkstra(h, w, t, n, sx, sy, gx, gy):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    initial_state = State(sx, sy, n, t[sy][sx])
    heapq.heappush(open_list, initial_state)

    if n > 0:
        initial_state_use_ticket = State(sx, sy, n - 1, 0)
        heapq.heappush(open_list, initial_state_use_ticket)

    while open_list:
        st = heapq.heappop(open_list)

        if st.x == gx and st.y == gy:
            return st.cost
        if st in closed:
            continue

        closed.add(st)

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]

            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list, State(nx, ny, st.ticket, ncost))

            if st.ticket > 0:
                ncost2 = st.cost
                heapq.heappush(open_list, State(nx, ny, st.ticket - 1, ncost2))

    return -1


h, w = map(int, input().split())
t = [[int(x) for x in input().split()] for _ in range(h)]
n = int(input())

cost = dijkstra(h, w, t, n, 0, 0, w - 1, h - 1)
print(cost)