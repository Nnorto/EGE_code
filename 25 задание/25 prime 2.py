"""
2) Найдите в диапазоне [2; 20000] числа,
 каждое из которых имеет максимальное количество простых делителей
  среди всех таких чисел. Выведите минимальное из таких чисел и
  через пробел количество его простых делителей.
"""

def prime(n):
    if n > 1:
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        return True
    else:
        return False

def vsedel(n):
    d = 1
    dell = []
    while d * d < n:
        if n % d == 0:
            if prime(d):
                dell.append(d)
            if prime(n // d):
                dell.append(n // d)
        d += 1
    if d * d == n and prime(d):
        dell.append(d)
    return dell

maxx = -1
c = 0
for i in range(2, 20000+1):
    if len(vsedel(i)) > 0:
        if maxx < len(vsedel(i)):
            maxx = len(vsedel(i))
            c = i
print(c, maxx)
