f = open('input.txt', 'r')
n, q = map(int, f.readline().split())
mas = list(map(int, f.readline().split()))
prefix = [0] * (len(mas) + 1)

for i in range(1, len(prefix)):
    prefix[i] = prefix[i-1] + mas[i-1]


for i in range(q):
    l, r = map(int, f.readline().split())
    print(prefix[r] - prefix[l] + mas[l-1])


f.close()