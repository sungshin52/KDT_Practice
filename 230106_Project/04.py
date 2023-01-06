fruits = {}

with open('data/fruits.txt', 'r', encoding = 'UTF8') as file:
    while True:
        line = file.readline()

        if not line:
            break

        else:
            if (line.strip() in fruits):
                fruits[line.strip()] += 1
            
            else:
                fruits[line.strip()] = 1

for key in fruits:
    print(f'{key} {fruits[key]}')