N = int(input())

if N % 3 == 0 and N % 5 == 0:
    print('FizzBuzz')
elif N % 3 == 0:
    print('Fizz')
elif N % 5 == 0:
    print('Buzz')
else:
    print(N)