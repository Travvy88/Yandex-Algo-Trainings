import pandas as pd



f = open('NetflixOriginals.csv', 'r')
s = f.read().replace("\"", "")
f.close()
with open('new.csv', 'w') as file:
    file.write(s)

df = pd.read_csv('new.csv', encoding='ANSI', on_bad_lines='warn')
print(df)