tree = []


def search(root, x):
    if not root:
        return 'NO'
    key, left, right = root
    if key == x:
        return 'YES'
    elif x < key:
        return search(left, x)
    elif x > key:
        return search(right, x)


def add(root, n):
    if not root:
        root.extend([n, None, None])
        return 'DONE'
    key, left, right = root
    if key == n:
        return 'ALREADY'
    elif n < key:
        if left is None:
            root[1] = [n, None, None]
            return 'DONE'
        else:
            return add(left, n)
    elif n > key:
        if right is None:
            root[2] = [n, None, None]
            return 'DONE'
        else:
            return add(right, n)


def printtree(root, depth=0):
    key, left, right = root
    if left:
        printtree(left, depth + 1)
    print(f"{''.join('.' * depth)}{key}")
    if right:
        printtree(right, depth + 1)


f = open('input.txt', 'r')
commands = f.readlines()
for command in commands:
    command_parts = command.split()

    if command_parts[0] == 'ADD':
        print(add(tree, int(command_parts[1])))
    elif command_parts[0] == 'SEARCH':
        print(search(tree, int(command_parts[1])))
    elif command_parts[0] == 'PRINTTREE':
        printtree(tree)
f.close()