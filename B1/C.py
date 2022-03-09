f = open('input.txt', 'r')
a, b, c = map(int, f.read().split())

if a > 12 and b <= 12:
    print(1)
elif a <= 12 and b > 12:
    print(1)
elif a == b:
    print(1)
else:
    print(0)


f.close()