def ss49(n):
    s = ''
    while n > 0:
        s = str(n % 49) + s
        n //= 49
    return s


num = abs(18* 7**108 - 5 * 49**76 + 343**35 - 50)  # подстава тут отрицательное число :)
s = ss49(num)
print(sum(list(map(int, s))))