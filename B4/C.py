f = open('input.txt', 'r')
text = f.read().split()
d = dict()
mas = []
for word in text:
    if word not in d.keys():
        d[word] = 0
    d[word] += 1


for word in d.keys():
    mas.append((d[word], word))
mas = sorted(mas, key=lambda x: (-x[0], x[1]))
for el in mas:
     print(el[1])

f.close()
