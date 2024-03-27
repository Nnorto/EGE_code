s = open('24 файл').readline()
s = s.split('X')
tk = k = 2
for i in range(k+1):
    tk = len(s[i])
maxk = tk
for i in range(1, len(s) - k):
    tk = tk - len(s[i-1]) + len(s[i+k])
    maxk = max(maxk, tk)
print(maxk)
