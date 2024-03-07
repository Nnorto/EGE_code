s = open('24.txt').readline()
s = s.replace('4', 'a')
s = s.replace('3', 'e')
m = 0
i = 0
for char in s:
    if (char == 'y' and i % 3 == 0) or \
       (char == 'a' and i % 3 == 1) or \
       (char == 'n' and i % 3 == 2) or \
       (char == 'd' and i % 3 == 3) or \
       (char == 'e' and i % 3 == 4) or \
       (char == 'e' and i % 3 == 4):
        i += 1
        m = max(i,m)
    elif char == 'y':
        i = 1
    else:
        i = 0
print(m)
