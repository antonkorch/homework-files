def read_from_file(filename):
    with open (filename) as f:
        lines = f.readlines()
    return lines

text = []
for i in range(1,4):
   filename = f'{i}.txt'
   text.append((read_from_file(filename), filename, len(read_from_file(filename))))

text.sort(key=lambda x: x[2])

with open ('result.txt', 'w') as f:
    for i in range (3):
        f.write(text[i][1] + '\n')
        f.write(str(text[i][2]) + '\n')
        for line in text[i][0]:
            f.write(line)
