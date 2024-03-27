a = list(map(int, open('17 задание/17 файлы/17-1.txt')))
c = 0
min_t5 = min([x for x in a if len(str(abs(x))) == 3 and abs(x) % 10 == 5])
max_s = -10**10
for i in range(len(a) - 1):
    n1 = a[i]
    n2 = a[i+1]
    if (100 <= abs(n1) <= 999) + (100 <= abs(n2) <= 999) == 1:
        s = n1 + n2
        if s % min_t5 == 0:
            c += 1
            max_s = max(max_s, s)
print(c, max_s)





