#submit
N = int(input())

user_bloodtype = {}
bloodtype_ftelling = {}

for i in range(N):
    key_value = input().split()
    user_bloodtype[key_value[0]] = key_value[1]

M = int(input())
for i in range(M):
    key_value = input().split()
    bloodtype_ftelling[key_value[0]] = key_value[1]

for k,v in user_bloodtype.items():
    for k1,v1 in bloodtype_ftelling.items():
        if v == k1:
            print(k + ' ' + v1)
    
#answer
n = int(input())
users = {}
for i in range(n):
    tmp = input().split()

    users[tmp[0]] = tmp[1]

m = int(input())
fortunes = {}
for i in range(m):
    tmp = input().split()

    fortunes[tmp[0]] = tmp[1]

for user, user_blood in users.items():
    for blood, fortune in fortunes.items():
        if user_blood == blood:
            print(user + " " + fortune)
            break