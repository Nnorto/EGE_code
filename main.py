s = open('24 пример файла').read()
k = 0
s = s.replace('W', 'X')
s = s.replace('V', 'X')
s = s.replace('Y', 'X')
s = s.replace('Z', 'X')
s = s.replace('XXX', 'XX XX')
s = s.replace('XXX', 'XX XX')
s = s.replace('XXX', 'XX XX')
s = s.split(' ')
print(len(max(s, key=len)) , s)


