s = open('24 файл').read()
count = 0
s = s.replace('W', 'X')
s = s.replace('V', 'X')
s = s.replace('Y', 'XX')
s = s.replace('Z', 'XX')
s = s.replace('XXX', 'XX XX')
s = s.replace('XXX', 'XX XX')
s = s.split(" ")
print(len(max(s, key=len)), s)
