def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True

def del_2(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            if prime(d) and prime(n // d):
                return True
        d += 1
    return False

k = 0
minn = 12122121121
for n in range(268312, 336492+1):
    if del_2(n):
        k += 1
        minn = min(minn, n)
print(k, minn)