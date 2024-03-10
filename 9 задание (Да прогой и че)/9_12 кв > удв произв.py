f = open("файлы/9_12")
count = 0
for i in f:
    a = [int(x) for x in i.split()]
    a.sort()
    if a[-1] ** 2 > 2 * a[0] * a[1]:
        count += 1
print(count)