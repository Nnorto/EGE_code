f = open('17 задание/17 файлы/17_31.txt')
a = list(map(int, f))
# min6 = 101010101010
# for x in a:
#     if abs(x) % 10 == 6:
#         min6 = min(min6, x)

min15 = max([x for x in a if abs(x) % 100 == 15])

count = 0
mins = 10**10

for i in range(len(a) - 2):
    if (1000<=abs(a[i])<=9999) + (1000<=abs(a[i+1])<=9999) + (1000<=abs(a[i+2])<=9999) == 1:
        s = a[i] + a[i+1] + a[i+2]
        if s < min15:
            count += 1
            mins = min(mins, s)


print(count, mins)



count = 0
mins = 10**10

for i in range(len(a) - 2):
    if (len(str(abs(a[i]))) == 4) + (len(str(abs(a[i+1]))) == 4) + (len(str(abs(a[i + 2]))) == 4) == 1:
        s = a[i] + a[i+1] + a[i+2]
        if s < min15:
            count += 1
            mins = min(mins, s)


print(count, mins)


min7 = -100010
for x in a:
    if abs(x) % 100 == 15:
        min7 = max(min7, x)

count = 0
mins = 1010
for i in range(len(a) - 2):
    if (len(str(abs(a[i]))) == 4)  + (len(str(abs(a[i + 1]))) == 4) + (len(str(abs(a[i + 2]))) == 4) == 1:
            s = a[i] + a[i+1] + a[i+2]
            if s < min7:
                count += 1
                mins = min(mins, s)

print(count, mins)
