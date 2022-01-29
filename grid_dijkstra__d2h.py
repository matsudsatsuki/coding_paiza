import heapq
dx = [1,0,-1,0]
dy = [0,-1,0,1]

class State:
    def __init__(self,x,y,cost):
        self.x = x
        self.y = y
        self.cost = cost
    def __hash__(self):
        return(self.x<<16) | self.y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __lt__(self,other):
        return self.cost < other.cost
    
def dijkstra(h,w,t,sx,sy,gx,gy):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    init_state = State(sx,sy,t[sy][sx])
    heapq.heappush(open_list,init_state)
    
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
            if not (0 <= nx <= w-1 and 0 <= ny <= h-1):
                continue
            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list,State(nx,ny,ncost))
    return -1

h,w = map(int,input().split())
t = [[int(x) for x in input().split()]for j in range(h)]

cost = dijkstra(h,w,t,0,0,w-1,h-1)

print(cost)
