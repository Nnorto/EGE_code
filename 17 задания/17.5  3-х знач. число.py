"""a = [int(s) for s in open("17 файлы/17_5.txt")]"""
a = list(map(int, open('17 файлы/17_5.txt')))
count = 0
min_5 = 333343333232334432
max_sum = -1
for x in range(len(a)):
    if a[x] % 10 == 5 and 99 < a[x] < 1000:
        min_5 = min(a[x], min_5)
print(min_5)

for i in range(len(a) - 1):
    if ((99 < a[i] < 1000) + (99 < a[i + 1] < 1000)) == 1:
        summa = a[i] + a[i + 1]
        print(summa%min_5)
        if summa % min_5 == 0:
            max_sum = max(max_sum, summa)
            count += 1

print(count, max_sum)
