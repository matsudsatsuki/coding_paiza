#submit code
S = input()
T = input()
count = 0

for i in range(len(T)-len(S)+1):
    cut = T[i:i+len(S)]
    
    if cut == S:
        count += 1

print(count)

#answer code
pattern = input()
string = input()
result = 0

for i in range(len(string) - len(pattern) + 1):
    portion = string[i : i + len(pattern)]

    if portion == pattern:
        result += 1

print(result)