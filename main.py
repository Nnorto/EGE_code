def f(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (x**2)**(n//2)
    return x * x ** (n - 1)

print(f(2, 10))