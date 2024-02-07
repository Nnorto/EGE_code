def jopa(n):
    vsd = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d % 10 == 9 and d != 9:
                vsd.append(d)
            if (n // d) % 10 == 9 and (n // d) != 0:
                vsd.append(n // d)
    return vsd

j = 0
for n in range(567000+1, 10**10):
    vsedel = jopa(n)
    if len(vsedel) > 0:
        print(n, vsedel[0])
        j += 1
        if j == 5:
            break


