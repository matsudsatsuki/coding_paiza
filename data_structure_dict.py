N,Q = map(int,input().split())

S = [input()for i in range(N)]
T = [input()for i in range(Q)]

for i in range(Q):
    if T[i] in S:
        print(S.index(T[i])+1)
    else:
        print(-1)

#sumple answer
N, Q = map(int, input().split())

S = {}
for i in range(N):
    s = input()
    if s not in S:
        S[s] = i + 1

for _ in range(Q):
    t = input()
    if t in S:
        print(S[t])
    else:
        print(-1)