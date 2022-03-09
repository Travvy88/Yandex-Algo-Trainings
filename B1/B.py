f = open('input.txt', 'r')
n, i, j = map(int, f.read().split())
po = abs(i - j) - 1
pr = abs(n - j - i + 1)

if po < 0:
    print(pr)

elif pr < 0:
    print(po)

else:
    print(min(po, pr))

print('po=', po)
print('pr=', pr)
f.close()