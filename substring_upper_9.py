#submit code
a,b = map(int,input().split())
S = str(input())

print(S[0:a-1], end='')
print(S[a-1:b].upper(),end='')
print(S[b:len(S)])

#answer code
nums = input().split()
string = input()

print(string[0 : int(nums[0]) - 1], end="")
print(string[int(nums[0]) - 1 : int(nums[1])].upper(), end="")
print(string[int(nums[1]) :])