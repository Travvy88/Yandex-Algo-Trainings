def add(root, parent, child):
    if not root:
        root.extend([parent, [[child, []]]])
        return
    nowparent, nowchildren = root
    if nowparent == parent:
        root[1].append([child, []])
    elif nowchildren:
        for children in nowchildren:
            add(children, parent, child)


def find(root, x):
    if not root:
        return 0
    nowparent, nowchildren = root
    if nowparent == x:
        return 1
    else:
        for children in nowchildren:
            res = find(children, x)
            if res == 1:
                return 1
        return 0

def check(root, anc, pred):
    if not root:
        return 0
    nowparent, nowchildren = root
    if nowparent == pred:
        for children in nowchildren:
            if find(children, anc) == 1:
                return 1
    else:
        for children in nowchildren:
            if check(children, anc, pred) == 1:
                return 1


'''
tree = []
add(tree, 1, 2)
add(tree, 1, 3)
add(tree, 2, 4)
add(tree, 3, 5)

print(tree)
print(find(tree, 22))
print(check(tree, 5, 1))
'''

tree = []
f = open('input.txt', 'r')
n = int(f.readline())
for i in range(n-1):
    line = f.readline().strip().split()
    add(tree, line[1], line[0])

# print(tree)
lines = f.readlines()
for line in lines:
    line = line.strip().split()
    if check(tree, line[1], line[0]) == 1:
        print(1, end=' ')
    elif check(tree, line[0], line[1]) == 1:
        print(2, end=' ')
    else:
        print(0, end=' ')

f.close()
