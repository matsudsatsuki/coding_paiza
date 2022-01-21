#submit
N = int(input())
inputs = {}
ans_dict = {}
for i in range(N):
    key_values = input().split()
    
    exist = False
    for (key,value) in inputs.items():
        if key == key_values[0]:
            exist = True
    if exist:
        inputs[key_values[0]] = inputs[key_values[0]] + int(key_values[1])
    else:
        inputs[key_values[0]] = int(key_values[1])

for (key,value) in inputs.items():
    ans_dict[value] = key

ans_dict = sorted(ans_dict.items(),reverse=True)

for i in ans_dict:
    print(i[1]+' '+str(i[0]))
    
#answer
num = int(input())
inputs = {}
result = {}

for i in range(num):
    tmp = input().split()

    exist = False
    for (key, value) in inputs.items():
        if key == tmp[0]:
            exist = True

    if exist:
        inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])
    else:
        inputs[tmp[0]] = int(tmp[1])

# ソート用にkeyとvalueを反転させた辞書を作る
for (key, value) in inputs.items():
    result[value] = key

result = sorted(result.items(), reverse=True)

for i in result:
    print(i[1] + " " + str(i[0]))