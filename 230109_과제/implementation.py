'''
# Q1

str = input('문자열을 입력하세요 > ')

for i in range(len(str)):
    if ('e' not in str):
        print('-1')
        break
    
    else:
        if (str[i] == 'e'):
            print(i)
            break

# Q2

str = input('문자열을 입력하세요 > ').split()
word_dict = {}

for word in str:
    if (word in word_dict):
        word_dict[word] += 1
    
    else:
        word_dict[word] = 1

for key in word_dict:
    print(f'{key} {word_dict[key]}')

# Q3

str = input('문자열을 입력하세요 > ')

for i in range(len(str)):
    if ('e' in str):
        if (str[i] == 'e'):
            str = str[:i] + str[i+1:]

print(str)

# Q4

str = input('문자열을 입력하세요 > ').split()

word = str[0]
alph = str[1]
count = 0

for alphabet in word:
    if (alphabet == alph):
        count += 1

print(count)

# Q5

str = input('문자열을 입력하세요 > ').split()
full_string = str[0] + '-'

for i in range(1, len(str)):
    if (i == len(str) - 1):
        full_string += str[i]
    
    else:
        full_string += str[i] + '-'

print(full_string)
'''
# Q6

num = int(input('양의 정수를 입력하세요 > '))
length_num = num
length = 0
sum = 0

if (num < 0):
    print(-1)

else:
    while (length_num > 0):
        length_num //= 10
        length += 1

    for i in range (length-1, -1, -1):
        sum += num // (10 ** i)
        num %= 10 ** i

    print(sum)
