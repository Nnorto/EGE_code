a = [int(s) for s in open("17 задания/17 файлы/17_5.txt")]
count = 0
min_5 = -1
max_sum = 0
for x in range(len(a)):
    if a[x] % 10 == 5 and len(str(a[x])) == 3:
        min_5 = min(a[x], min_5)
for i in range(len(a) - 1):
    if ((len(str(a[i])) == 3) + (len(str(a[i + 1])) == 3)) == 1:
        summa = a[i] + a[i + 1]
        if summa % min_5 == 0:
            max_sum = max(max_sum, summa)
            count += 1

print(count, max_sum)
