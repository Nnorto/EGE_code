a = list(map(int, open('17 задание/17 файлы/17statokt23.txt')))

max_17 = -10**10
for x in a:
    if x % 100 == 17:
        max_17 = max(max_17, x)

k = 0
max_s = -10**10

for i in range(len(a) - 2):
    if (1000<= a[i] <=9999) + (1000<= a[i + 1] <=9999) + (1000<= a[i + 2] <=9999) == 2:
        if (a[i] % 5 == 0) + (a[i + 1] % 5 == 0) + (a[i + 2] % 5 == 0) >= 1:
            summa = a[i] + a[i + 1] + a[i + 2]
            if summa > max_17:
                k += 1
                max_s = max(max_s, summa)

print(k, max_s)