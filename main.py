a = list(map(int, open("17 задание/17 файлы/17_5.txt")))

max_e = -10**11
for el in range(len(a)):
    if a[el] % 10 == 2:
        max_e = max(max_e, a[el])

jopa = 10 ** 11
count = 0
for i in range(len(a) - 1):
    if (a[i] % 10 == 0) + (a[i + 1] % 10 == 0) == 1:
        summ = a[i] + a[i + 1]
        if summ < max_e:
            count += 1
            jopa = min(jopa, summ)

print(count, jopa)