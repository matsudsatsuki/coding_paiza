phone_num = input()
#print(phone_num)
count = 0
for num in phone_num:
    if num  == '0':
        count += 12*2
    if num == '1':
        count += 3*2
    if num == '2':
        count += 4*2
    if num == '3':
        count += 5*2
    if num == '4':
        count += 6*2
    if num == '5':
        count += 7*2
    if num == '6':
        count += 8*2
    if num == '7':
        count += 9*2
    if num == '8':
        count += 10*2
    if num == '9':
        count += 11*2

print(count)
        
    