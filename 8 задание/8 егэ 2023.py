from itertools import *

count = 0
for x in product("01234567", repeat=5):
    s = ''.join(x)
    if len(set(s)) == len(s) and s[0] != '0':  # len(set(s)) == len(s) все числа различные
        s = s.replace('3', '1').replace('5', '1').replace('7', '1')
        s = s.replace('0', '2').replace('4', '2').replace('6', '2')
        if '11' not in s and '22' not in s:
            count += 1

print(count)