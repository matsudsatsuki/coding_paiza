import heapq

H,W = map(int,input().split())
S = [list(input())for i in range(W)]

#print(S)
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
    
def dyn_dijkstra(h,w,t,sx,sy,gx,gy):
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
      
n = H   
graph = [[1]*n for i in range(n)]
for i in range(H):
    for j in range(W):
        if S[j][i] == '#':
            graph[j][i] = 1000
            #graph[i][j] = 1
        
q = []
heapq.heapify(q)

state_2 = State(3,1,graph[3][1])
heapq.heappush(q,state_2)
closed = set()
move_list = []
while q:
    st_2 = heapq.heappop(q)
    move_list.append(st_2)
    if st_2 in closed:
        continue
    closed.add(st_2)
    for i in range(4):
        nx = st_2.x + dx[i]
        ny = st_2.y + dy[i]
        if not (0 <= nx <= W-1 and 0 <= ny <= H-1):
            continue
        ncost = st_2.cost + graph[ny][nx]
        heapq.heappush(q,State(nx,ny,ncost))
    
    