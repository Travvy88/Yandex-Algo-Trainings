f = open('input.txt', 'r')
n = map(int, f.readline())
mas = list(map(int, f.readline().split()))


def createprefixsum(mas):
    prefix = [0] * (len(mas) + 1)
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + mas[i-1]
    return prefix


def findsum(l, r, prefix):
    return prefix[r + 1] - prefix[l]


maxsum = mas[0]
prefixsum = createprefixsum(mas)
print(mas)
print(prefixsum)


for l in range(len(prefixsum)):
    for r in range(l, len(prefixsum) - 1):
        maxsum = max(maxsum, findsum(l, r, prefixsum))

print(maxsum)
f.close()