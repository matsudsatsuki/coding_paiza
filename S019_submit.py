import heapq
import itertools
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
    initial_state = State(sx, sy, t[sy][sx])
    heapq.heappush(open_list, initial_state)

    costs = [0] * w
    while open_list:
        st = heapq.heappop(open_list)
        if st in closed:
            continue
        closed.add(st)

        if st.y == gy and st.x == gx:
            #costs[st.x] = st.cost-1
            cost = st.cost-1

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]
            if nx < 0:
                nx = w-1
            if nx > w -1:
                nx = 0
            if ny < 0:
                ny = h-1
            if ny > h-1:
                ny = 0
            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):#ここを弄れば、上下左右の移動ができるはず
                continue

            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list, State(nx, ny, ncost))

    return cost

n, h, w = map(int, input().split())
t = [[1]*w]*h

town_list = []
for i in range(n):
    x,y = map(int,input().split())
    town_list.append([x-1,y-1])#0origin
distance_list = []

graph = [[] for _ in range(n)]
memo = []

q = []
#heapq.heapify(q)
dis = 0
i = 0
j = 1
while i < n-1:
    dis = dijkstra(h,w,t,town_list[i][0],town_list[i][1],town_list[j][0],town_list[j][1])
    q.append(dis)
    j += 1
    if j == n:
        i += 1
        j = i+1
        

    
#print(q)      
a = list(itertools.combinations(q,n-1))
#print(a)    
#print(min(q))
ans = 1000   
for i in a:
    s = sum(list(i))
    ans = min(ans,s)
    
    
    
print(ans)