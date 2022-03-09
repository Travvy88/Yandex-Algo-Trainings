f = open('input.txt', 'r')
lst = map(int, f.readline().split())
s = set()
for el in lst:
    if el in s:
        print('YES')
    else:
        print('NO')
    s.add(el)

f.close()
