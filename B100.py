N = int(input())
time_list = [list(input().split())for i in range(N)]
#print(diff)
Q = int(input())

accurate_score = []
displayed_score = []
diff_score = []

on_time = [int(input())for i in range(Q)]

for i in range(max(on_time)):
    accurate_score.append(0)
    displayed_score.append(0)
    diff_score.append(0)

for time in range(max(on_time)):
    for j in range(3):
        if time+1 == int(time_list[j][0]):
            accurate_score[time] = int(time_list[j][2])
            if time+2 != int(time_list[j+1][0]):
                accurate_score[time+1] = int(time_list[j][2])
            else:
                continue
        else:
            continue

print(accurate_score)
#give up