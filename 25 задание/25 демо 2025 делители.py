def vsedel(n):
    vd = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            if d * d == n:
                vd.append(d)
            else:
                vd.append(d)
                vd.append(n//d)
        d += 1
    return vd

m = 0
count = 0
for n in range(800_001, 10**10):
    if len(vsedel(n)) > 0:
        m = max(vsedel(n)) + min(vsedel(n))
    if m % 10 == 4:
        count += 1
        print(n, m)
        if count == 5:
            break

