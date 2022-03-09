f = open('input.txt', 'r')
print(len(set(map(int, f.readline().split())) & set(map(int, f.readline().split()))))
f.close()
