f = open('input.txt', 'r')

ms = map(int, f.read().split())
col = dict()
col[0] = 0
col[1] = 0
col[2] = 0
l = []
s = ''
for el in ms:
    col[el] += 1
    l.append(el)
    s += str(el)

pos1 = ['111000000', '000111000', '000000111', '100100100', '010010010', '001001001', '100010001', '001010100']
pos2 = ['222000000', '000222000', '000000222', '200200200', '020020020', '002002002', '200020002', '002020200']

for p in pos:
    if p == s


f.close()