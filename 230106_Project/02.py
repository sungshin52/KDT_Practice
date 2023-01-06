count = 0

with open('data/fruits.txt', 'r', encoding = 'UTF8') as file:
    while True:
        line = file.readline()

        if not line:
            break
        else:
            count += 1

print(count)