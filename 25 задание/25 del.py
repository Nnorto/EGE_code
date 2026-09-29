def vse_del(n):
    vd = [1, n]
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d * d == n:
                vd.append(d)
            else:
                vd.append(d)
                vd.append(n // d)
    return vd


for num in range(10_271_400, 10272500+1):
    all_del = vse_del(num)
    if len(all_del) == 4:
        print(num)