# Q1
num = int(input('정수를 입력하세요 > '))

if (num > 0):
    print('True')
else:
    print('False')

print('\n')

# Q2
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if (num1 > num2):
    print(num1)
elif (num1 < num2):
    print(num2)
else:
    print('False')

print('\n')

# Q3
num = int(input('정수를 입력하세요 > '))

if ((num > 1) & (num < 10)):
    print(True)
else:
    print(False)

print('\n')

# Q4
num = int(input('정수를 입력하세요 > '))

if ((num > 0) & (num%2 == 0)):
    print(True)
else:
    print(False)

print('\n')

# Q5
num = int(input('정수를 입력하세요 > '))

if ((num >= 60) & (num <= 100)):
    print('합격')
elif ((num >= 0) & (num < 60)):
    print('불합격')
else:
    print('에러')

print('\n')

# Q6
string = input('문자열을 입력하세요 > ')

for i in range(-1, -len(string)-1, -1):
    print(string[i])

print('\n')

# Q7
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if (num1 > num2):
    for i in range(num2 + 1, num1):
        print(i)
elif (num1 < num2):
    for i in range(num1 + 1, num2):
        print(i)
else:
    print("False")

print('\n')

# Q8
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if (num1 > num2):
    for i in range(num1 - 1, num2, -1):
        print(i)
elif (num1 < num2):
    for i in range(num2 - 1, num1, -1):
        print(i)
else:
    print('False')

print('\n')

# Q9
num = int(input('정수를 입력하세요 > '))

if (num < 1):
    print('False')
    exit()

for i in range(1, num):
    if (i%2 == 0):
        continue
    else:
        print(i)

print('\n')


# Q10
N = 10
M = 10

for n in range(2, N):
    for m in range(2, M):
        print(f'{n} X {m} = {n*m}')

print('\n')