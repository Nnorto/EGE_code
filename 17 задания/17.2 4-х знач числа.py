a = []
for s in open("17 файлы/17_2.txt"):
    a.append(int(s))

count = 0
max_25 = -1
max_sum = 0
for x in range(len(a)):
    if a[x] % 100 == 25:
        max_25 = max(a[x], max_25)
for i in range(len(a) - 2):
    if ((len(str(abs(a[i]))) == 4) + (len(str(abs(a[i+1]))) == 4) + (len(str(abs(a[i+2]))) == 4)) >= 2:
        summa = a[i] + a[i + 1] + a[i + 1]
        if summa < max_25:
            max_sum = max(max_sum, summa)
            count += 1

print(count, max_sum)
