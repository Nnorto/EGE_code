"""
20 задание
x – 1 куча
y – 2 куча
p – чей ход
"""


def f(x, y, p):
    if x + y >= '% сумма %' and p == '% чей ход выигрывает (ВТОРОЙ)%':
        return True
    if x + y < '% сумма %' and p == '% чей ход выигрывает (ВТОРОЙ) %':
        return False
    if x + y >= '%сумма%':
        return False
    if p % 2 == 1:  # если ход не наш
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1)  # здесь какие ходы могут быть
    else:  # если ход нащ
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1)  # здесь какие ходы могут быть


for i in range(1, 44):  # Диапазон S
    if f(5, i, 0):  # 0 - ничей ход, 1 – Петя, 2 – Ваня, 3 – Петя и тд
        print(i)
