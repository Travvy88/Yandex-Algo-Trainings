f = open('input.txt', 'r')
s = f.readline().strip()


def check(s):
    summa = 0
    for ch in s:
        if ch == '(':
            summa += 1
        else:
            summa -= 1

        if summa < 0:
            return 'NO'
    if summa == 0:
        return 'YES'
    else:
        return 'NO'


print(check(s))
f.close()