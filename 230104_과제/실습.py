# Q1
num = int(input('정수를 입력하세요 > '))

if (num >= 0):
    print(num)
else:
    print(-num)

print('\n')

# Q2
number_list = [1, 2, 3, 4, 5]
count = 0

for i in number_list:
    count += 1

print(count)

print('\n')

# Q3
number_list = [1, 2, 3, 4, 5]
sum = 0


for element in number_list:
    sum += element

print(sum)

print('\n')

# Q4
num_list = [2, 4, 6]
count = 0
sum = 0

for element in num_list:
    count += 1
    sum += element

average = sum/count

print(average)

print('\n')

# Q5
number_list = [1, 2, 3, 4, 5]
mul = 1

for element in number_list:
    mul *= element

print(mul)

print('\n')

# Q6
number_list = [1, 2, 3, 4, 5]
i = 1
max = number_list[0]

while (i < len(number_list)):
    if (number_list[i] > max):
        max = number_list[i]
    i += 1
    
print(max)

print('\n')

# Q7
number_list = [1, 2, 3, 4, 5]
i = 1
min = number_list[0]

while (i < len(number_list)):
    if (number_list[i] < min):
        min = number_list[i]
    i += 1

print(min)

print('\n')
