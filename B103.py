N = int(input())
x_R,x_G,x_B = map(int,input().split())
flag = True
ans = 0
for i in range(N):
    direction,color = map(str,input().split())
    if direction == 'R':
        if color == 'R':
            x_R += 1
        if color == 'G':
            x_G += 1
        if color == 'B':
            x_B += 1
        if color == 'Y':
            x_R += 1
            x_G += 1
        if color == 'M':
            x_R += 1
            x_B += 1
        if color == 'C':
            x_G += 1
            x_B += 1
        if color == 'W':
            x_R += 1
            x_B += 1
            x_G += 1
    if direction == 'L':
        if color == 'R':
            x_R -= 1
        if color == 'G':
            x_G -= 1
        if color == 'B':
            x_B -= 1
        if color == 'Y':
            x_R -= 1
            x_G -= 1
        if color == 'M':
            x_R -= 1
            x_B -= 1
        if color == 'C':
            x_G -= 1
            x_B -= 1
        if color == 'W':
            x_R -= 1
            x_B -= 1
            x_G -= 1
    if x_R == x_B and x_B == x_G and flag:
        ans = x_R
        flag = False
        
        
        
if flag:
    print('no')
else:
    print(ans)
# "R", "G", "B", "Y", "M", "C", "W" のいずれかで、それぞれライトを赤、緑、青、黄、マゼンタ、シアン、白