# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from collections import defaultdict
from itertools import chain



def tr(G):
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def match(G,X,Y):
    H = tr(G)
    S,T,M = set(X),set(Y),set()
    while S:
        s = S.pop()
        Q,P ={s},{}
        while Q:
            u = q.pop()
            if u in T:
                T.remove(u)
                break
            forw = (v for v in G[u] if (u,v) not in M)
            back = (v for v in H[u] if (v,u) not in M)
            for v in chain(forw,back):
                if v in P:
                    P[v] = u
                    Q.add(v)
            while u != s:
                u,v = P[u],u
                if v in G[u]:
                    M.add((u,v))
                else:
                    M.remove((v,u))
    return M

#submit(B_rank)
import collections


def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False
 
 
# 標準入力からのグラフ読み取り
dog_n, monk_n, com = map(int, input().split())
edges = [set() for _ in range(dog_n)]


matched = [-1] * monk_n
 
for _ in range(com):
    x, y = map(int, input().split())
    edges[x-1].add(y-1)
    #edges[y-1].add(x-1)
#print(edges)
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる

#print(edges)
first_score = sum(dfs(s, set()) for s in range(dog_n))+1

while True:
    if set() in edges:
        edges.remove(set())
    else:
        break

a = list(edges)
#print(a)
for i in range(len(edges)):
    edges[i] = list(edges[i])
l = ['a','a']

#print(edges)
ne = []
for i in range(len(edges)):
    ne.append(''.join(map(str,edges[i])))
#print(ne)
b = collections.Counter(ne)
c = b.most_common()[0][1]
second_score = c + monk_n
third_score = dog_n
ans = max(first_score,second_score,third_score)
print(ans)




n,m,r = map(int,input().split())
if n > m:
    N = n
if n < m:
    N = m
else:
    N = n
graph = [[0]*N for _ in range(N)]
for _ in range(r):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    #graph[b-1][a-1] = 1  # 有向グラフなら消す
#print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]
match(graph,n,m)












