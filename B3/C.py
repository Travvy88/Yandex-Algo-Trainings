f = open('input.txt', 'r')
d = dict()
for el in map(int, f.readline().split()):
    if el not in d.keys():
        d[el] = 0
    d[el] += 1

for key in d.keys():
    if d[key] == 1:
        print(key, end=' ')

f.close()
