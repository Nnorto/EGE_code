def f(x, y, pl, pr):

    if x > y:
        return 0

    if x == y:
        return 1
    if pl == 2:
        return f(x * 2, y, 0, pr + 1)
    if pr == 2:
        return f(x + 1, y, pl + 1, 0)

    return f(x + 1, y, pl + 1, 0) + f(x * 2, y, 0, pr + 1)


print(f(1, 16, 0, 0))