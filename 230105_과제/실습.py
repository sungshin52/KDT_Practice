# Q1

str1 = input('문자열을 입력하세요 > ')
count = 0

for element in str1:
    if element == 'e':
        count += 1

print(count)

print('\n')

# Q2

str1 = input('문자열을 입력하세요 > ')
alph = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
count = 0

for str in str1:
    if str in alph:
        count +=1

print(count)

print('\n')

# Q3

dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

age = 2023 - int(dict_variable['생년']) + 1

print(f'나이 : {age}세')

print('\n')

# Q4

dict_info = {}

name = input('이름을 입력하세요 > ')
phone = input('전화번호를 입력하세요 > ')
addr = input('거주지를 입력하세요 > ')

dict_info["이름"] = name
dict_info["전화번호"] = phone
dict_info["거주지"] = addr

print(dict_info)

for key in dict_info:
    print(f'{key} : {dict_info[key]}')

print('\n')

# Q5

dict_person = {}
dict_info = {}

name = input('이름을 입력하세요 > ')
phone = input('전화번호를 입력하세요 > ')
email = input('이메일을 입력하세요 > ')
addr = input('거주지를 입력하세요 > ')

dict_info["전화번호"] = phone
dict_info["이메일"] = email
dict_info["거주지"] = addr

dict_person["정우영"] = dict_info

print(dict_person)

print('\n')

# Q6

dict_alph = {}

string = input('문자열을 입력하세요 > ')

for char in string:
    dict_alph[char] = string.count(char)

for key in dict_alph:
    print(key, dict_alph[key])

