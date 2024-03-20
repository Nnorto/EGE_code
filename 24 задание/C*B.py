f = open('24 файл')
count = 0
for s in f:
    for x in range(len(s) - 2):
        if s[x] == 'C' and s[x + 2] == 'B':
            count += 1
            print(s[x], s[x+1], s[x+2])
            break
print(count)

