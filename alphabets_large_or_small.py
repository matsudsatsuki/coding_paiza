#submit(score90)
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

X = input()
Y = input()
C = input()
flag = 0

for i in range(alphabet.index(X),alphabet.index(Y)):
    if alphabet[i] == C:
        flag = 1

if flag == 1:
    print('true')
else:
    print('false')

#answer
first = input()
last = input()
pattern = input()

alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
result = "false"

in_a_range = False
for alphabet in alphabets:
    if first == alphabet:
        in_a_range = True

    if in_a_range and pattern == alphabet:
        result = "true"

    if last == alphabet:
        break

print(result)