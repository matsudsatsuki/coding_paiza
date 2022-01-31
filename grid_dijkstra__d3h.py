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
        return (self.x<<16) | self.y
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
T = [[int(x) for x in input().split()]for _ in range(H)]

        
        
#print(T)   
st = dijkstra(H,W,T,0,0,W-1,H-1)
print(st.cost)

while st is not None:
    print(st.y, st.x)
    st = st.ref
    
    
    