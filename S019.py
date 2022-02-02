from copy import deepcopy
import heapq

class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
    
    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        #self.adjacency_dict[v2].append(v1)
    def remove_edge(self, v1, v2):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)
    def remove_vertex(self,v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]
    #def weight(self,v1,v2):
        #self.adjacency_dict
    def print_graph(self):
        print(self.adjacency_dict)
        
        
def cal_distance(G,v1,v2):
    x_dis = abs(v2-v1)
    y_dis = abs(G[v2]-G[v1])
    return x_dis+y_dis
    
inf = float('inf')
def relax(w,u,v,D,P):
    d = D.get(u,inf) + W[u][v]
    if d < D.get(v,inf):
        D[v],P[v] = d,u
        return True

def dijkstra(G,s):
    D,P,Q,S = {s:0},{},[(0,s)],set()
    while Q:
        _,u = heappop(Q)
        if u in S:continue
        S.add(u)
        for v in G[u]:
            relax(G,u,v,D,P)
            heappush(Q,(D[v],v))
    return D,P
        
    
    
    
    
def bellman_ford(G,s):
    D,P = {s:0},{}
    for rnd in G:
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G,u,v,D,P):
                    changed = True
        if not changed: break
    else:
        raise ValueError('negative cycle')
    return D,P
def johnson(G):
    G = deepcopy()
    s = object()
    G[s] = {v:0 for v in G}
    h, _ = bellman_ford(G,s)
    del G[s]
    for u in G:
        for v in G[u]:
            G[u][v] += h[u]-h[v]
    D,P = {},{}
    for u in G:
        D[u],P[u] = dijkstra(G,u)
        for v in G:
            D[u][v] += h[v]-h[u]
    return D
    
    
N,H,W = map(int,input().split())
graph = Graph()

for i in range(1,max(H,W)+1):
    graph.add_vertex(i)
    
for i in range(N):
    x,y = map(int,input().split())
    graph.add_edge(x,y)
    

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

def dijkstra(h, w, t, sx, sy, gy):
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

        if st.y == gy:
            costs[st.x] = st.cost

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]
            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list, State(nx, ny, ncost))

    return costs


h, w = map(int, input().split())
t = [[int(x) for x in input().split()] for _ in range(h)]

costs = dijkstra(h, w, t, 0, 0, h - 1)
for cost in costs:
    print(cost)
