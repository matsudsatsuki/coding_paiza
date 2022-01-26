#submit(fail)
n, m = map(int, input().split())
graph = [[-1]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    #graph[v-1].append([u-1, w])  # 有向グラフなら消す
# [[2, 3], [3, 1], [5, 9]], ..., [...]]
for i in range(n):
    flag = True
    for j in range(n):
        if graph[i][j] != -1:
            print(graph[i][j])
            flag = False
        elif j == n-1 and graph[i][j] == -1 and flag:
            print(graph[i][j])