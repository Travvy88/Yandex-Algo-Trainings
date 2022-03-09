f = open('input.txt', 'r')
n = int(f.readline())
s = 0
for el in map(int, f.readline().split()):
    s += el
result = s / n
if result % 1 == 0.5:
    if result >= 0:
        result = result // 1 + 0.51
    else:
        result = result // 1 - 0.51
print(round(result))
print(result)
# print(round(-2.5 // 1 - 0.51))



f.close()