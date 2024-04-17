f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 97
maxs = 0
maxost = [0] * k
for i in a:
    ost = i % k
    ostnap = (k-ost) % k
    if i > maxost[ostnap]:
        maxs = max(maxs, maxost[ostnap] + i)
    maxost[ost] = max(maxost[ost], i)

print(maxs)