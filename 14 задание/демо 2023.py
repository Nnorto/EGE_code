n = 1331**6500 - 55 * 121**610 + 77 * 11 ** 510 - 3 * 11 ** 100 - 221
c = 0
while n > 0:
    if n % 11 == 10:
        c += 1
    n //= 11
print(c)

n1 = 1331**6500 - 55 * 121**610 + 77 * 11 ** 510 - 3 * 11 ** 100 - 221
arr = []
while n1 > 0:
    arr.append(str(n1 % 11))
    n1 //= 11
print(arr.count('10'))
