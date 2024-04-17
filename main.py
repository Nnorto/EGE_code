f = open('17 задание/17 файлы/17_32.txt')
a = list(map(int, f))
# min6 = 101010101010
# for x in a:
#     if abs(x) % 10 == 6:
#         min6 = min(min6, x)

max19 = max([x for x in a if x % 100 == 19])

count = 0
maxs = -10**10
for i in range(len(a) - 2):
    if (len(str(a[i])) == 4) + (len(str(a[i + 1])) == 4) + (len(str(a[i + 2])) == 4) == 2:
            if (a[i] % 3 == 0) + (a[i+1] % 3 == 0) + (a[i+2] % 3 == 0) >= 1:
                s = a[i] + a[i+1] + a[i+2]
                if s > max19:
                    count += 1
                    maxs = max(maxs, s)
print(count, maxs)

count = 0
maxs = -10**10
for i in range(len(a) - 2):
    if (len(str(a[i])) == 4) + (len(str(a[i + 1])) == 4) + (len(str(a[i + 2])) == 4) == 2:
            if (a[i] % 3 == 0) + (a[i+1] % 3 == 0) + (a[i+2] % 3 == 0) >= 1:
                s = a[i] + a[i+1] + a[i+2]
                if s > max19:
                    count += 1
                    maxs = max(maxs, s)
print(count, maxs)