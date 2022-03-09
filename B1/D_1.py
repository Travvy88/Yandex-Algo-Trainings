f = open('input.txt', 'r')
n = int(f.readline())
l = list(map(int, f.readline().split()))
k = n // 2
print(l[k])

f.close()