N,Q = map(int,input().split())

A = [int(x)for x in input().split()]

for _ in range(Q):
    query = [int(x) for x in input().split()]
    
    cmd = query[0]
    if cmd == 0:
        A.append(query[1])
    elif cmd == 1:
        del A[len(A)-1]#pop()でよかった
    else:
        print(' '.join(map(str,A)))