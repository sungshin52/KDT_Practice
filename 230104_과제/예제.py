# Q1

list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")
    
"""
예측을 작성하세요.
2 3 4 5 7 8
"""
print('\n')

# Q2
for element in range(-2, 10, 2):
    print(element, end=" ")
    
"""
예측을 작성하세요.
-2 0 2 4 6 8
"""

print('\n')

# Q3
a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
        
    if number % 3 == 0:
        b = b + 1
        
    if number % 4 == 0:
        c = c + 1
        
    if number % 5 == 0:
        d = d + 1

print(a, b, c, d) # 5 4 3 2

print('\n')

# Q4
i = 0
while i <= 10:
    print(i)
    i = i + 1
"""
예측을 작성하세요.
0
1
2
3
4
5
6
7
8
9
10
"""

print('\n')

# Q5
i = 0
while i <= 10:
    i = i + 1
    print(i)
"""
예측을 작성하세요.
1
2
3
4
5
6
7
8
9
10
11
"""

print('\n')

# Q6
i = 0
while i <= 10:
    i = i + 2
    print(i)
"""
예측을 작성하세요.
2
4
6
8
10
12
"""

print('\n')

# Q7
i = 0
while True:
    print(i) 
    i = i + 1
    if i > 10:
        break
"""
예측을 작성하세요.
0
1
2
3
4
5
6
7
8
9
10
"""

print('\n')

# Q8
i = 0
while True:
    print(i) 
    if i > 10:
        break
    i = i + 1
    
"""
예측을 작성하세요.
0
1
2
3
4
5
6
7
8
9
10
11
"""

print('\n')

# Q9
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7

print('\n')

# Q10
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21

print('\n')

# Q11
list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12

print('\n')