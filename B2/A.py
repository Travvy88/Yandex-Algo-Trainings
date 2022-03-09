f = open('input.txt', 'r')

line = int(f.readline())

mx = line
cnt = 0
while line != 0:
    if line > mx:
        mx = line
        cnt = 1
    elif line == mx:
        cnt += 1

    line = int(f.readline())
print(cnt)
f.close()
