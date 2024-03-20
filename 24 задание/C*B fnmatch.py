import fnmatch, string

f = open('24 пример файла')
k = 0
for s in f:
    for x in range(len(s) - 2):
        if s[x] == 'C' and s[x + 2] == 'B':
            k += 1
            break


print(k)

f = open('24 пример файла')
k = 0
for s in f:
    if fnmatch.fnmatch(s, '*C?B*'):
        k += 1
print(k)


alf = string.ascii_uppercase
f=open('24 пример файла')
c=0
for s in f:
    for a in alf:
        if "C"+str(a)+"B" in s:
            c+=1
print(c)
