a = list(map(int, open("17 файлы/17_5.txt")))
count = 0
mins = 10**10
max2 = -1
for x in range(len(a)):
    if a[x] % 10 == 2:
        max2 = max(max2, a[x])

for i in range(len(a) - 1):
    if (a[i] % 10 == 0 and a[i+1] % 10 != 0) or (a[i] % 10 != 0 and a[i+1] % 10 == 0):
        if (a[i] + a[i+1]) < max2:
            count += 1
            mins = min(a[i] + a[i+1], mins)

print(count, mins)


