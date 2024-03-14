import string

s = open('24 файл').readline()
a = []
for i in range(len(a) - 1):
    if s[i] == 'E':
        a.append(s[i + 1])
alf = string.ascii_uppercase
maxk = 0
for x in alf:
    if a.count(x) > maxk:
        maxk = a.count(x)
        res = x

print(res, maxk)