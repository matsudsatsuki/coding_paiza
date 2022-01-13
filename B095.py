N,M = map(int,input().split())
Hz = list(input() for i in range(M))
Hz_list = [[input() for i in range(M)]for j in range(N)]
base_score = 100
error = 0
scores = [[i for i in range(M*N)]for j in range(N)]
for i in range(N):
    for j in range(M):
        error = abs(int(Hz[j])-int(Hz_list[i][j]))
        if error <= 10 and error > 5:
            base_score -= 1
            scores[i][j] = base_score
        elif error <= 20 and error > 10:
            base_score -= 2
            scores[i][j] = base_score
        elif error <= 30 and error > 20:
            base_score -= 3
            scores[i][j] = base_score
        elif error > 30:
            base_score -= 5
            scores[i][j] = base_score
        else:
            scores[i][j] = base_score
        #print(scores[i][j])

max_ele = [[i for i in range(M)]for j in range(N)]
result = [1000 for i in range(N)]
for i in range(N):
    for j in range(M):
        if result[i] > scores[i][j]:
            result[i] = scores[i][j]
        else:
            continue

print(max(result))         
            