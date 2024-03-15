from itertools import *
count = 0
for x in product("ABCX", repeat=5):
    s = ''.join(x)
    if (s.count('X') == 1 and s[-1] == 'X') or ('X' not in s):
        count += 1

print(count)