a = list(map(int, open("17 задание/17 файлы/17-1.txt")))

max_s = -10**10
count = 0
for i in range(len(a)-1):
    if (abs(a[i]) % 3 == 0) + (abs(a[i + 1]) % 3 == 0) >= 1:
        s = a[i] + a[i + 1]
        count += 1
        max_s = max(max_s, s)

print(count, max_s)