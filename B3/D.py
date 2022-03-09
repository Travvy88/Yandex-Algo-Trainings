f = open('input.txt', 'r')
n = int(f.readline())
line = f.readline()
final = set(range(1, n + 1))
while line.rstrip() != 'HELP':
    s = set(map(int, line.split()))
    answer = f.readline().rstrip()
    if answer == 'YES':
        final.intersection_update(s)
    if answer == 'NO':
        final.difference_update(s)

    line = f.readline()

print(*sorted(final))
f.close()
