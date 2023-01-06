str_list = ['Hello, Python!\n', '1일차 파이썬 공부 중\n',
            '2일차 파이썬 공부 중\n', '3일차 파이썬 공부 중\n'
            '4일차 파이썬 공부 중\n', '5일차 파이썬 공부 중\n']

with open('data/01.txt', 'w', encoding = 'UTF8') as file:
    file.writelines(str_list)