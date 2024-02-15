def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True

def sums(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def mapsum(n):
    return sum(list(map(int, str(n))))

for n in range(120120, 230230+1):
    if prime(n) and mapsum(n) >= 44:
        print(n, sums(n))