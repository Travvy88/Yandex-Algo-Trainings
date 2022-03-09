import codecs

f = codecs.open('input.txt', 'r', encoding='utf8')
n = int(f.readline())

msgs = [''] * (n + 1)  # темы сообщений
themes = dict()  # темы и количество сообщений
for i in range(1, n + 1):
    x = int(f.readline())
    if x == 0:
        theme = f.readline().rstrip()

        themes[theme] = 1
        msgs[i] = theme
    else:
        theme = msgs[x]
        msgs[i] = theme
        themes[theme] += 1

    text = f.readline().rstrip()

print(max(themes, key=themes.get))
f.close()
