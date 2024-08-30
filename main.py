f = open('24 пример файла')
c = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    b = []
    for i in a:
        b.append(a.count(i))
    if b.count(3) == 3 and b.count(1) == 3:
        sump = 0
        sumnp = 0
        for i in range(len(a)):
            if b[i] == 3:
                sump += a[i]
        for i in range(len(a)):
            if b[i] == 1:
                sumnp += a[i]
        if sump ** 2 > sumnp ** 2:
            c += 1

print(c)


for x in range(2030):
    c = 7 ** 170 + 7 ** 100 - x
    s = ""
    while c > 0:
        s = str(c % 7) + s
        c //= 7
    if s.count('0') == 71:
        print(x)
