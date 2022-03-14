f = open('input.txt', 'r')
s = int( f.readline())

a = list(map(int, f.readline().split()))[1:]
b = list(map(int,  f.readline().split()))[1:]
c = list(map(int,  f.readline().split()))[1:]


def tuples(array):
    tuplz = []
    for i in range(len(array)):
        tuplz.append((array[i], i))
    return tuplz




def check(a, b, c, s):
    a = tuples(a)
    b = tuples(b)
    c = tuples(c)
    a.sort()
    b.sort()
    c.sort()
    maximum = ''.join((str(len(a)), str(len(b)), str(len(c))))
    minimum = maximum

    for ai, i in a:
        cpos = len(c) - 1
        bpos = 0
        summa = ai + b[bpos][0] + c[cpos][0]
        while bpos < len(b) and cpos >= 0:
            if summa < s:
                bpos += 1
            elif summa > s:
                cpos -= 1
            elif summa == s:
                list(map(int, [i, b[bpos][1], c[cpos][1]]))
                current = ''.join(list(map(str, [i, b[bpos][1], c[cpos][1]])))
                if current < minimum:
                    minimum = current

                # ijk.append((i, b[bpos][1], c[cpos][1]))
                cpos -= 1

            if bpos < len(b) and cpos >= 0:
                summa = ai + b[bpos][0] + c[cpos][0]

    return minimum, maximum


minimum, maximum = check(a, b, c, s)
if minimum == maximum:
    print(-1)
else:
    print(' '.join(minimum))
f.close()

