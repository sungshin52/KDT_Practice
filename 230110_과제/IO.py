# Q1

a = int(input())
print(a)

# Q2

string = input().split()

for str in string:
    print(str, end = ' ')

print('\n')

# Q3

T = int(input())

for t in range(1, T+1):
    num = int(input())
    print(num)

# Q4

num = list(map(int, input().split()))

for i in range(len(num)):
    print(num[i], end = ' ')

print('\n')

# Q5

a, b = list(map(int, input().split()))

print(a, b)

# Q6

string = input().split()

for str in string:
    print(str, end = ' ')

print('\n')

# Q7

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    
    for i in range(len(num)):
        print(num[i], end = ' ')
    print('\n')

# Q8

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))

    for i in range(len(num)):
        print(num[i], end = ' ')
    print('\n')
