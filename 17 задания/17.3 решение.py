f = open("17 задания/17 файлы/17_5.txt")
a = []
for s in f:
    a.append(int(s))

count = 0
minar = 10 ** 10
for i in range(len(a) - 2):
    if (abs(a[i]) % 14 == 0 or abs(a[i + 1]) % 14 == 0 or abs(a[i + 2]) % 14 == 0) \
            and (abs(a[i]) % 4 == 0 and abs(a[i + 1]) % 4 == 0 and abs(a[i + 2]) % 4 == 0):
        sr = (a[i] + a[i + 1] + a[i + 2]) // 3
        minar = min(minar, sr)
        count += 1

print(count, minar)
