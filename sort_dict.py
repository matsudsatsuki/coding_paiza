#submit
N = int(input())
my_dict = {}

for i in range(N):
    key_value = input().split()
    #print(key_value)
    my_dict[int(key_value[1])] = key_value[0]

my_dict = sorted(my_dict.items())

for i in my_dict:
    print(i[1])
#print(my_dict)

#answer
num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])
