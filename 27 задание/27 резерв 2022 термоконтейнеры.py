f = open("27 пример")
n = int(f.readline())
a = [int(x) for x in f]
max_1 = max_2 = maxs = 0
for i in range(2, n):
    max_1 = max(max_1, i - 2)
    max_2 = max(max_2, max_1- a[i - 1]*2) # ОН ВЫЧИТАЕТСЯ ДВАЖДЫ
    maxs = max(max_2 + a[i], maxs)

print(maxs)