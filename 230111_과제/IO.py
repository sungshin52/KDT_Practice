# Q1

nums = list(map(int, input().split()))

for num in nums:
    print(num, end = ' ')

print('\n')

# Q2

string = input().split()

for str in string:
    print(str, end = ' ')

print('\n')

# Q3

T = int(input())    # test case
print(T)

for t in range(1, T+1):
    N = int(input())    # input line num
    print(N)

    for n in range(N):
        num = int(input())
        print(num)

# Q4

T = int(input())
print(T)

for t in range(1, T+1):
    N = int(input())
    print(N)

    for n in range(N):
        nums = list(map(int, input().split()))

        for num in nums:
            print(num, end = ' ')
        print('\n')

# Q5

import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
print(T)

for t in range(1, T+1):
    N = int(input())
    print(N)

    for n in range(N):
        string = input().split()

        for str in string:
            print(str, end = ' ')

        print('\n')

# Q6

sys.stdin = open("input2.txt", "r")

T = int(input())
print(T)

for t in range (1, T+1):
    N = int(input())
    print(N)

    for n in range (N):
        nums = list(map(int, input().split()))

        for num in nums:
            print(num, end = ' ')

        print('\n')

# Q7

T, N = list(map(int, input().split()))
print(T, N)

for t in range (1, T+1):
    for n in range (N):
        num = int(input())

        print(num)

# Q8

T, N = list(map(int, input().split()))
print(T, N)

for t in range (1, T+1):
    for n in range (N):
        nums = list(map(int, input().split()))

        for num in nums:
            print(num, end = ' ')
        print('\n')

# Q9
#import sys
sys.stdin = open("input3.txt", "r")

T, N = list(map(int, input().split()))
print(T, N)

for t in range (1, T+1):
    for n in range (N):
        nums = list(map(int, input().split()))

        for num in nums:
            print(num, end = ' ')
        print('\n')