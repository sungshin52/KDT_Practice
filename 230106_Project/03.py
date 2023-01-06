fruits = []
count = 0

with open('data/fruits.txt', 'r', encoding = 'UTF8') as file:
    while True:
        line = file.readline()

        if not line:
            break

        elif ('berry' in line):
            if (line.strip() not in fruits):
                if(line.strip().endswith('berry')):
                    count += 1
                    fruits.append(line.strip())

print(count)

for fruit in fruits:
    print(fruit)