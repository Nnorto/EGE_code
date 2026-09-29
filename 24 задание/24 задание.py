s = open('files/24_23206.txt').readline()
c = ''
m = 0
for r in range(len(s)):
    c += s[r]
    if c[-1] in '02468':
        c = c[-1]
    if c.count('S') == 35:
        m = max(len(c), m)
    if r % 1_000_000 == 0:
        print(r, len(s), m)
print(m)