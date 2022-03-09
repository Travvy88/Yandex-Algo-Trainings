f = open('input.txt', 'r')

l = list(map(int, f.read().split()))
r = -1
rmin = 11
rmas = []
for i in range(len(l)):

    if l[i] == 1:
        rmin = 11
        for k in range(len(l)):
            if l[k] == 2:
                r = abs(i - k)
                if r < rmin:
                    rmin = r
        rmas.append(rmin)

print(max(rmas))
f.close()
