f = open('input.txt')
s = f.readline().rstrip()
ln = len(s)
money = 0
m = int(ln / 2)
if ln % 2 == 0:
    for i, j in zip(range(0, m), reversed(range(m, ln))):
        if s[i] != s[j]:
            money += 1
else:
    for i, j in zip(range(0, m), reversed(range(m + 1, ln))):
        if s[i] != s[j]:
            money += 1

print(money)
f.close()