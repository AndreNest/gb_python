file = '/Users/andrejnesterov/Desktop/GB/GB_Python/sem_04/less_03/file.txt'
f = open(file, 'r')
data = f.read() + ' '
f.close()

number = []

while data != '':
    spase_pos = data.index(' ')
    number.append(int(data[:spase_pos]))
    data = data[spase_pos + 1:]

out = []
for e in number:
    if not e % 2:
        out.append((e,e**2))
print(out)