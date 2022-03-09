f = open('input.txt', 'r')
m = int(f.readline())

max_count = 0
sawers = []
numbers = dict()
for i in range(m):
    sawers.append(set(f.readline().rstrip()))

n = int(f.readline())
for i in range(n):
    number = f.readline().rstrip()
    setnum = set(number)
    numbers[number] = 0
    for j in range(m):
        if sawers[j] <= setnum:
            numbers[number] += 1

    if numbers[number] > max_count:
        max_count = numbers[number]


for key in numbers.keys():
    if numbers[key] == max_count:
        print(key)


f.close()
