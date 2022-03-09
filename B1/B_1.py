f = open('input.txt', 'r')
n, i, j = map(int, f.read().split())
if i <= j:
    mi = i
    ma = j
else:
    mi = j
    ma = i

po = ma - mi - 1
pr = n - ma + mi - 1


print(min(po, pr))

print('po=', po)
print('pr=', pr)
f.close()